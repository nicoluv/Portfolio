from io import BytesIO
import os
import datetime
import glob
import operator
import os.path

import PIL
import cv2
import shutil

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage  # image upload code
from django.contrib import messages
import io

from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import random
import string
from PIL import Image

from docx2pdf import convert
from .forms import MyModelForm
# Create your views here.
from .models import Upload
from .tokens import generate_token
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mysite import settings

DOCUMENTS_CHOICES = (
    ('firma', 'FIRMA'),
    ('texto', 'TEXTO'),
)


def home(request):
    try:
        if request.user.is_authenticated:
            return index(request, username=request.user.username)
        else:
            return render(request, "authentication/index.html")
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def signup(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('home')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!!")
                return redirect('home')

            if len(username) > 20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('home')

            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                return redirect('home')

            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('home')

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            # myuser.is_active = False
            myuser.is_active = False
            myuser.save()
            messages.success(request,
                             "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

            # Welcome Email
            subject = "Bienvenid@ a REID - Django Login!!"
            message = "Hola " + myuser.first_name + "!! \n" + "Bienvenid@ Reid!! \nGracias por visitar nuestra pagina web\n. También le hemos enviado un correo electrónico de confirmación, por favor confirme su dirección de correo electrónico. \n\nAgradeciéndote\nREID"
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirma tu Email @ REID - Django Login!!"
            message2 = render_to_string('email_confirmation.html', {

                'name': myuser.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()

            return redirect('signin')

        return render(request, "authentication/signup.html")

    except Exception as e:
        return render(request, 'pages-misc-error.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request, 'activation_failed.html')


def signin(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                request.session['username'] = user.username
                form = MyModelForm
                # fname = user.first_name
                # messages.success(request, "Logged In Sucessfully!!")
                # return render(request, "authentication/index.html",{"fname":fname})
                return index(request, username=user.username)  # pass username to index function
            else:
                messages.error(request, "Bad Credentials!!")
                return redirect('home')

        return render(request, "authentication/signin.html")

    except Exception as e:
        return render(request, 'pages-misc-error.html')


def load_images_from_folder(img_dir):
    data_path = os.path.join(img_dir, '*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        img = cv2.imread(f1)
        data.append(img)
    return data


def signout(request):
    try:
        logout(request)
        messages.success(request, "Logged Out Successfully!!")
        return redirect('home')
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def get_random_name(file_name):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(10))
    _, ext = os.path.splitext(file_name)
    return random_name + ext


def findNewestDir(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)

    lister = sorted(dirs.items(), key=operator.itemgetter(1))
    return lister[-1][0]

def findNewestOCR(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)

    lister = sorted(dirs.items(), key=operator.itemgetter(1))
    return lister[-1][0]


def findNewestImg(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)

    lister = sorted(dirs.items(), key=operator.itemgetter(1))
    return lister


def findSecondNewestDir(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)

    lister = sorted(dirs.items(), key=operator.itemgetter(1))
    return lister[-2][0]

def findSecondNewestOCR(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)

    lister = sorted(dirs.items(), key=operator.itemgetter(1))
    return lister[-2][0]


def index(request, username=None):
    try:
        form = MyModelForm()
        context = {'form': form, 'username': username} if username else {'form': form}
        return render(request, 'index.html', context)
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                try:
                    total += get_directory_size(entry.path)
                except FileNotFoundError:
                    pass
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


# @csrf_protect
def result(request):
    try:
        if request.method == 'POST':
            # Get the posted form and files
            form = MyModelForm(request.POST)
            myfile = request.FILES.get('uploadDocument', None)
            myfile2 = request.FILES.get('uploadDocument2', None)
            answer = request.POST.get('tipo_documento')

            # Check if "firma" was selected and get the word input
            # if answere == "firma" and answer == "firma":
            word = request.POST.get('floatingInput', '')
            logo = "ouricon.png"

            # Generate random names for the files
            name1 = get_random_name(myfile.name) if myfile else None
            name2 = get_random_name(myfile2.name) if myfile2 else None

            # Save the files with the random names
            fs = FileSystemStorage()
            filename1 = fs.save(name1, myfile) if name1 else None
            filename2 = fs.save(name2, myfile2) if name2 else None

            # Get the User object for the logged-in user
            user = request.user

            # Create a new Upload object with the saved file names and associated User object
            obj = Upload(user=user, image1=filename1, image2=filename2, documento=answer, word=word)
            value = obj.save()

            # Set the path to the folder where you want to save the PDFs
            # file_path = os.path.join(os.getcwd(),f'media/Users/{user}/Reports/People', word)
            file_path = os.path.join(settings.MEDIA_ROOT, f'Users/{user}/Reports/People', word)

            # Check if the folder exists, and if not, create it
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            # Set the filename for the PDF (you will need to customize this according to your needs)
            if myfile is None:
                filename = f'report-{name2}'
            else:
                filename = f'report-{name1}'

            # Create a file path by joining the folder path and the filename
            file_path = os.path.join(file_path, filename)

            # generate the file
            # Create a file-like buffer to receive PDF data.
            buffer = io.BytesIO()

            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer)

            # Get the username from the session
            username = request.session.get('username')
            IMAGESIZE = (2 * cm, 2 * cm)

            # p.drawString(10, 800, f'Your file is uploaded and saved with random names. Username: {username}')

            # im = Image(logo, 2 * inch, 2 * inch)
            # Story.append(im)

            now = datetime.datetime.now()
            p.setFont('Helvetica', 12)
            p.drawString(360, 800, "Reporte generado el " + now.strftime("%d/%m/%Y"))

            # fp = open("src/uploads/static/assets/img/favicon/favicon.ico", "rb")
            # img = PIL.Image.open(fp)
            p.setFont('Helvetica', 24)
            # p.drawInlineImage( os.path.join(os.getcwd(),"uploads\\static\\assets\\img\\favicon\\iconsmall.png"),210, 790 - IMAGESIZE[0], IMAGESIZE[0], IMAGESIZE[1])
            p.drawString(210, 750, 'Reporte | Reid')

            p.setFont('Helvetica', 18)
            p.drawString(80, 725, 'Reconocimiento e Identificación de Escritua a Mano')
            p.setStrokeColor("#71C2FF")
            p.line(20, 700, 580, 700)
            p.setStrokeColor("#000000")
            p.setFont('Helvetica', 12)

            working_d = os.getcwd();
            img_path = os.path.join(settings.MEDIA_ROOT, f'images')
            newImg = findNewestImg(img_path)

            print("the new img is" , newImg)

            images_dir = "../media/images"
            input_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), images_dir
            )

            img_complete= os.path.join(os.getcwd(), newImg[-1][0]) + "\\" + newImg[-1][0] + "_0.jpg"
            img_complete2= input_path + "\\" +newImg[-2][0] + "\\"+newImg[-2][0] + "_0.jpg"
            # img_complete = working_d + "\\media\\images\\" + newImg[-1][0] + "\\*.jpg"
            # img_complete2 = working_d + "\\media\\images\\" + newImg[-2][0] + "\\*.jpg"
            print("the new img_complete is", img_complete)
            print("the new img_complete2 is", img_complete2)

            if myfile2 is None and myfile is not None:
                return redirect('home')

            if answer == 'firma':

                ocr_dir = f"Users/admin/Signatures/temp/OCR_Results"

                ocr_path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), ocr_dir
                )

                newDirPath = findNewestOCR(ocr_path)
                newDirPath2 = findSecondNewestOCR(ocr_path)

                dir1 = os.path.join(
                    os.getcwd() , newDirPath
                )

                dir2 = os.path.join(
                    os.getcwd(), newDirPath2
                )

                images_dir = f"../uploads/Users/admin/Signatures/temp/Cleaned_Results"

                mypath2 = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), images_dir
                )
                newDir = findNewestDir(mypath2)
                newDir2 = findSecondNewestDir(mypath2)
                print("The newest directory is", newDir)
                print("The second newest directory is", newDir2)

                newDir_value = newDir.split('_')
                newDir2_value = newDir2.split('_')
                print("nombre del doc", newDir2_value[-2])

                print("este es el dir1" + dir1)
                print("este es el dir2" + dir2)


                if not os.listdir(dir1) :
                    imgpath = os.path.join(os.getcwd(), newDir) + "\Cleaned_Results_LineSweep_Results_" + newDir_value[
                        -1] + "_0.jpg"
                else:
                    imgpath = os.path.join(os.getcwd(), newDir) + "\Cleaned_Results_LineSweep_Result_OCR_Result_" + \
                              newDir_value[-1] + "_0.jpg"

                if not os.listdir(dir2):
                    imgpath2 = os.getcwd() + '\\' + newDir2 + "\Cleaned_Results_LineSweep_Results_" + newDir2_value[
                        -1] + "_0.jpg"
                else:
                    imgpath2 = os.getcwd() + '\\' + newDir2 + "\Cleaned_Results_LineSweep_Result_OCR_Result_" + newDir2_value[-1] + "_0.jpg"


                if not os.listdir(dir1) or not os.listdir(dir2):

                    print("Contains mix")
                    print("el img path2 es ", imgpath2)
                    print("el img path1 es", imgpath)

                    if myfile2 is not None:

                        p.drawString(65, 500,
                                     'La escritura bajo sospecha siguiente, presentada como firma, fue encontrada en el documento ')

                        p.drawString(65, 485,
                                     'titulado ' + myfile2.name)

                    else:
                        p.drawString(65, 500,
                                     'La escritura bajo sospecha siguiente, presentada como firma, fue encontrada en el documento ')

                        p.drawString(65, 485,
                                     'mostrado. ')

                    if myfile is not None:
                        p.drawString(65, 640,
                                     'La escritura original siguiente, presentada como firma, fue encontrada en el documento')
                        p.drawString(65, 625,
                                     ' titulado ' + myfile.name)

                        p.drawImage(imgpath2, 65, 515, width=260, preserveAspectRatio=True, mask='auto')

                    else:
                        p.drawString(65, 640,
                                     'La escritura original siguiente, presentada como firma, fue encontrada en el documento')
                        p.drawString(65, 625,
                                     ' mostrado')



                    p.drawImage(imgpath, 65, 370, width=260, preserveAspectRatio=True, mask='auto')

                    accuracy = value

                    p.drawString(65, 345,
                                 'El documento de la escritura original junto con el de la escritura bajo sospecha ha sido')
                    p.drawString(65, 330,
                                 'sometido a un análisis por parte de la herramienta de reconocimiento e identificación de')
                    p.drawString(65, 315,
                                 f'escritura Reid, resultando en un {accuracy:.2f}% de similitud entre ambas firmas.')

                    p.setStrokeColor("#71C2FF")
                    p.line(20, 80, 580, 80)
                    p.setStrokeColor("#000000")

                    p.drawString(510, 60, "Página 1/2")

                    p.save()



                else:

                    # C:\Users\Nicole Urena\PycharmProjects\another\ProyectoFinalCarrera\src\uploads\Users\admin\Signatures\temp\Cleaned_Results\Cleaned_Results_nkxohqnogi.pdf\Cleaned_Results_LineSweep_Results_nkxohqnogi.pdf_0.jpg
                    # src/uploads/Users/admin/Signatures/temp/Cleaned_Results/Cleaned_Results_gimxvgwkri.pdf
                    print("el img path2 es ", imgpath2)
                    print("el img path1 es", imgpath)

                    if myfile is not None:

                        p.drawString(65, 640,
                                     'La escritura original mostrada a continuación ha sido extraída del cheque que le sigue,')
                        p.drawString(65, 625,
                                     'y proviene de un documento titulado ' + myfile.name)
                    else:
                        p.drawString(65, 640,
                                     'La escritura original mostrada a continuación ha sido extraída del cheque que le sigue,')

                    if myfile2 is not None:
                        p.drawString(65, 260,
                                     'La escritura bajo sospecha presentada a continuación ha sido extraída del cheque que  ')
                        p.drawString(65, 245, 'le sigue, y proviene del documento titulado ' + myfile2.name)
                    else:
                        p.drawString(65, 260,
                                     'La escritura bajo sospecha presentada a continuación ha sido extraída del cheque que  ')


                    print(imgpath2)
                    p.drawImage(imgpath2, 55, 510, width=260, preserveAspectRatio=True, mask='auto')
                    p.drawImage(img_complete2, 55, 200, width=500, height=400, preserveAspectRatio=True, mask='auto')




                    p.drawImage(imgpath, 65, 120, width=260, preserveAspectRatio=True, mask='auto')

                    p.setStrokeColor("#71C2FF")
                    p.line(20, 80, 580, 80)
                    p.setStrokeColor("#000000")

                    p.drawString(510, 60, "Página 1/2")

                    p.showPage()

                    p.drawImage(img_complete, 55, 480, width=500, height=400, preserveAspectRatio=True, mask='auto')

                    accuracy = value

                    p.drawString(65, 535,
                                 'El documento de la escritura original junto con el de la escritura bajo sospecha ha sido')
                    p.drawString(65, 520,
                                 'sometido a un análisis por parte de la herramienta de reconocimiento e identificación de')
                    p.drawString(65, 505,
                                 f'escritura Reid, resultando en un {accuracy:.2f}% de similitud entre ambas firmas.')

                    p.setStrokeColor("#71C2FF")
                    p.line(20, 80, 580, 80)
                    p.setStrokeColor("#000000")
                    p.drawString(510, 60, "Página 2/2")
                    p.drawString(65, 330, '')

                    p.save()


            # TEXTO

            else:
                # intento2
                print("The img_complete original is", img_complete2)

                p.drawImage(img_complete2, 55, 300, width=500, height=350, preserveAspectRatio=True, mask='auto')

                p.drawString(65, 640,
                             'La escritura original mostrada a continuación ha sido extraída de un documento ')
                p.drawString(65, 625,
                             'titulado ' + myfile.name)

                # esto tiene las coordenadas del logo
                # p.drawInlineImage(imgpath[-1], 65,650 - IMAGESIZE[0], IMAGESIZE[0]*2 , IMAGESIZE[1]*2)

                p.drawString(65, 280,
                             'La escritura bajo sospecha presentada a continuación ha sido extraída del documento ')
                p.drawString(65, 265, 'titulado ' + myfile2.name)

                p.setStrokeColor("#71C2FF")
                p.line(20, 80, 580, 80)
                p.setStrokeColor("#000000")

                p.drawString(510, 60, "Página 1/2")

                p.showPage()
                print("The img_complete2 is", img_complete)

                p.drawImage(img_complete, 55, 480, width=500, height=400, preserveAspectRatio=True, mask='auto')

                accuracy = value

                # p.drawString(65, 400, 'Ha sido comparada con la escritura bajo sospecha  ')
                p.drawString(65, 535,
                             'El documento de la escritura original junto con el de la escritura bajo sospecha ha sido')
                p.drawString(65, 520,
                             'sometido a un análisis por parte de la herramienta de reconocimiento e identificación de')
                p.drawString(65, 505,
                             f'escritura Reid, resultando en un {accuracy:.2f}% de similitud entre ambos documentos.')

                p.setStrokeColor("#71C2FF")
                p.line(20, 80, 580, 80)
                p.setStrokeColor("#000000")
                p.drawString(510, 60, "Página 2/2")
                p.drawString(65, 330, '')

                # Close the PDF object cleanly, and we're done.

                p.save()

                # FileResponse sets the Content-Disposition header so that browsers
                # present the option to save the file.
                # buffer.seek(0)

                # Write the buffer contents to a file

            with open(file_path, 'wb') as f:
                f.write(buffer.getbuffer())

            file_url = os.path.join(settings.MEDIA_ROOT, f"Users/{user}/Reports/People/{word}", filename)
            response = HttpResponse(open(file_url, 'rb').read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

        else:
            form = MyModelForm()

        return render(request, 'my_template.html', {'form': form})

    except Exception as e:
        return render(request, 'pages-misc-error.html')


def signatures(request):
    try:
        user = request.user.username
        path = f"Users/{user}/Signatures/People"
        input_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), path
        )
        if not os.path.exists(input_path):
            os.makedirs(input_path)

        folders = []
        search_query = request.GET.get('search', '')  # Get search query from GET parameters
        for folder in os.listdir(input_path):
            if os.path.isdir(os.path.join(input_path, folder)):
                if search_query:  # Check if search query is not empty
                    if search_query.lower() in folder.lower():  # Case-insensitive search
                        folders.append(folder)
                else:  # If search query is empty, show all folders
                    folders.append(folder)

        paginator = Paginator(folders, 10)  # Paginate the folders with 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'search_query': search_query
        }
        return render(request, 'Signatures.html', context=context)
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def images(request, folder):
    try:
        if request.method == 'GET':
            user = request.user.username
            path = os.path.join('Signatures', 'People', folder)
            input_path = os.path.join(settings.MEDIA_ROOT, 'Users', user, path)

            images = []
            for file in os.listdir(input_path):
                if file.endswith('.jpg') or file.endswith('.png'):
                    images.append(os.path.join(settings.MEDIA_URL, 'Users', user, path, file))

            paginator = Paginator(images, 5)  # limit 5 images per page
            page = request.GET.get('page')

            try:
                images = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                images = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                images = paginator.page(paginator.num_pages)

            context = {
                'images': images,
                'folder': folder
            }
            return render(request, 'Images.html', context=context)

    except Exception as e:
        return render(request, 'pages-misc-error.html')



def people(request):
    try:
        user = request.user.username
        people_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'Users/{user}/Texts/People')

        # Check if the folder exists
        if not os.path.exists(people_folder):
            # If the folder doesn't exist, create it
            os.makedirs(people_folder)

        # Get search query parameter
        search_query = request.GET.get('q', '')

        # Filter people list based on search query
        if search_query:
            people_list = [p for p in os.listdir(people_folder) if search_query.lower() in p.lower()]
        else:
            people_list = os.listdir(people_folder)

        # Pagination
        paginator = Paginator(people_list, 10)  # Display 10 people per page
        page = request.GET.get('page')
        people_list = paginator.get_page(page)

        return render(request, 'people.html', {'people_list': people_list, 'search_query': search_query})
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def person(request, person_name):
    try:
        if request.method == 'GET':
            user = request.user.username
            person_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         f'Users/{user}/Texts/People/{person_name}/Classified_Letters')
            person_list = os.listdir(person_folder)
            return render(request, 'person.html', {'person_name': person_name, 'person_list': person_list})
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def letter(request, person_name, letter_name):
    try:
        if request.method == 'GET':
            user = request.user.username
            letter_folder = os.path.join(settings.MEDIA_ROOT,
                                         f'Users/{user}/Texts/People/{person_name}/Classified_Letters/{letter_name}')

            # Generate a list of image URLs
            images = []
            for file in os.listdir(letter_folder):
                if file.endswith('.jpg') or file.endswith('.png'):
                    images.append(os.path.join(settings.MEDIA_URL, 'Users', user, 'Texts', 'People', person_name,
                                               'Classified_Letters', letter_name, file))

            # Pass the image URLs to the template context
            context = {
                'person_name': person_name,
                'letter_name': letter_name,
                'images': images,
            }
            return render(request, 'letter.html', context=context)
    except Exception as e:
        return render(request, 'pages-misc-error.html')


def reporte(request):
    try:
        if request.method == 'GET':
            user = request.user.username
            path = f"Users/{user}/Reports/People"
            input_path = os.path.join(settings.MEDIA_ROOT, path)
            if not os.path.exists(input_path):
                os.makedirs(input_path)

            search = request.GET.get('search', '')  # Get search query from request
            folders = []

            if search:
                # If search query is not empty, filter folders based on search query
                folders = [folder for folder in os.listdir(input_path) if search.lower() in folder.lower()]
            else:
                # If search query is empty, show all folders
                folders = os.listdir(input_path)

            # Paginate the folders list with 10 folders per page
            paginator = Paginator(folders, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'page_obj': page_obj,
                'search': search
            }
            return render(request, 'reportes.html', context=context)

    except Exception as e:
        return render(request, 'pages-misc-error.html')


def docs(request, folder):
    try:
        if request.method == 'GET':
            user = request.user.username
            path = os.path.join('Reports', 'People', folder)
            input_path = os.path.join(settings.MEDIA_ROOT, 'Users', user, path)

            # Update your logic here to get the list of PDF files
            pdf_files = []
            for file in os.listdir(input_path):
                if file.endswith('.pdf'):
                    pdf_files.append(os.path.join(settings.MEDIA_URL, 'Users', user, path, file))

            # Paginate the list of PDF files
            paginator = Paginator(pdf_files, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'page_obj': page_obj,
                'folder': folder
            }
            return render(request, 'doc.html', context=context)

    except Exception as e:
        return render(request, 'pages-misc-error.html')

def convert_to_pdf(request):
    try:
        # Check if the 'temp' and 'pdf' folders exist, and create them if not
        temp_folder = os.path.join(settings.MEDIA_ROOT, 'temp')
        pdf_folder = os.path.join(settings.MEDIA_ROOT, 'pdf')
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder)

        if request.method == 'POST':
            # Get the file from the request object
            file = request.FILES['uploadDocument']

            # Save the uploaded file to a temporary location
            temp_file_path = os.path.join(temp_folder, file.name)

            with open(temp_file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Create the output file path
            output_file_path = os.path.join(pdf_folder, os.path.splitext(file.name)[0] + '.pdf')

            # Convert the file to PDF using the appropriate library
            if file.name.endswith('.docx'):
                convert(temp_file_path, output_file_path)
            elif file.name.endswith('.jpg'):
                img = Image.open(temp_file_path)
                img.save(output_file_path, 'PDF', resolution=100.0)
            else:
                raise ValueError('Unsupported file format')

            # Delete the temporary file
            os.remove(temp_file_path)

            # Return the PDF file as a response
            with open(output_file_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(output_file_path) + '"'
                return response

        return render(request, 'convert_to_pdf.html')

    except Exception as e:
        return render(request, 'pages-misc-error.html')
def under_maintenance(request):
    return render(request, "pages-misc-under-maintenance.html")

