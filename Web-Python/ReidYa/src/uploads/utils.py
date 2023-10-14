import shutil

import cv2
import re
from pdf2image import convert_from_path
import numpy as np
from skimage.color import label2rgb
from skimage.measure import regionprops
import matplotlib.pyplot as plt
from skimage import measure, morphology
try:
    from PIL import Image, ImageEnhance
except ImportError:
    import Image

import pytesseract
import os
from skimage import transform, exposure
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# TODO add contour detection for enhanced accuracy
s1 = ''
s2 = ''
s3 = ''
info = []

def OCR(name, opcion, user):
    global s1
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    sign = 0
    total_files = 0
    processed_files = 0
    images_dir = "../media/images/"+name
    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), images_dir
    )
    for filename in os.listdir(input_path):
        total_files = total_files + 1
        if ".jpg" in filename:
            print("OCR Processing file -", filename)
            img = cv2.imread(os.path.join(input_path, filename))
            img = cv2.resize(img, (1280, 589))
        else:
            continue
        h, w, _ = img.shape  # assumes color image
        # Get verbose data including boxes, confidences, line, page numbers and text
        data = pytesseract.image_to_data(Image.open(os.path.join(input_path, filename)))
        if opcion == 'firma':
            # Search for the word "firma" in the data
            found_firma = False
            for d in data.splitlines():
                d = d.split("\t")
                print(str(len(d)) + '-' + str(d) + '-' + str(d[6]))
                if len(d) == 12 and re.search(r'\bfirma\b', d[11], re.IGNORECASE):
                    # Extract the signature from the bounding box of the word "firma"
                    found_firma = True
                    signCd = [int(d[6]), int(d[7]), int(d[8]), int(d[9])]
                    lengthSign = signCd[0] + signCd[3] - signCd[1]
                    lengthSignCd = [int(signCd[0] - lengthSign * 2.7), int(signCd[1] - lengthSign * 2.5)]
                    scaleY = 2
                    scaleXL = 2.5
                    scaleXR = 0.5
                    img = cv2.rectangle(
                        img,
                        (lengthSignCd[0], lengthSignCd[1]),
                        (
                            lengthSignCd[0] + int((scaleXL + scaleXR + 1) * lengthSign),
                            lengthSignCd[1] + int(scaleY * lengthSign),
                        ),
                        (255, 255, 255),
                        2,
                    )
                    cropImg = img[
                              lengthSignCd[1]: (lengthSignCd[1]) + int(scaleY * lengthSign),
                              lengthSignCd[0]: lengthSignCd[0] + int((scaleXL + scaleXR + 1) * lengthSign),
                              ]
                    mainpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Signatures/temp/OCR_Results")
                    if not os.path.exists(mainpath):
                        os.makedirs(mainpath)
                    path = os.path.join(mainpath, "OCR_Results_"+name)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    s1 = "OCR_Result_" + filename
                    if cropImg.size != 0:
                        processed_files = processed_files + 1
                        cv2.imwrite(os.path.join(path, s1), cropImg)
                        # Increment the sign count
                        sign = sign + 1

            # If the word "firma" is not found, crop the image the same as the first time
            if not found_firma:
                signCd = [0, int(h / 2), w, int(h / 2)]
                lengthSign = signCd[0] + signCd[3] - signCd[1]
                lengthSignCd = [int(signCd[0] - lengthSign * 2.7), int(signCd[1] - lengthSign * 2.5)]
                scaleY = 2
                scaleXL = 2.5
                scaleXR = 0.5
                img = cv2.rectangle(
                    img,
                    (lengthSignCd[0], lengthSignCd[1]),
                    (
                        lengthSignCd[0] + int((scaleXL + scaleXR + 1) * lengthSign),
                        lengthSignCd[1] + int(scaleY * lengthSign),
                    ),
                    (255, 255, 255),
                    2,
                )
                cropImg = img[
                          lengthSignCd[1]: (lengthSignCd[1]) + int(scaleY * lengthSign),
                          lengthSignCd[0]: lengthSignCd[0] + int((scaleXL + scaleXR + 1) * lengthSign),
                          ]
                mainpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Signatures/temp/OCR_Results")
                if not os.path.exists(mainpath):
                    os.makedirs(mainpath)
                path = os.path.join(mainpath, "OCR_Results_"+name)
                if not os.path.exists(path):
                    os.makedirs(path)
                s1 = "OCR_Result_" + filename
                if cropImg.size != 0:
                    processed_files = processed_files + 1
                cv2.imwrite(os.path.join(path, s1), cropImg)
                # Increment the sign count
                sign = sign + 1

                if not found_firma or cropImg.size == 0:
                    return False


    # Print the results
    print("Total files processed: ", processed_files, "/", total_files)
    info.append(processed_files)
    info.append(total_files)
    if opcion == 'firma':
        print("Total signatures found: ", sign)
        info.append(sign)

# inicializamos la lista de puntos de referencia y booleano indicando si se está recortando o no
ref_point = []
cropping = False

def crop_images_in_directory(input_path, image_name, user, name):

    temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), input_path)

    img = cv2.imread(os.path.join(temp_path, image_name))

    rect_color = (0, 255, 0)
    def shape_selection(event, x, y, flags, param):
        # grab references to the global variables
        global ref_point, cropping
        # if the left mouse button was clicked, record the starting (x, y) coordinates and indicate that cropping is being performed
        if event == cv2.EVENT_LBUTTONDOWN:
            ref_point = [(x, y)]
            cropping = True
        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that the cropping operation is finished
            ref_point.append((x, y))
            cropping = False
            # draw a rectangle around the region of interest
            cv2.rectangle(clone, ref_point[0], ref_point[1], rect_color, 2)
            cv2.imshow("image", clone)
            cv2.waitKey(1)  # Add a short delay to allow window to update
            cv2.waitKey(2000)  # Add a longer delay to keep the rectangle visible for 2 secondsv2.waitKey(0)

    clone = img.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", shape_selection)
    # add scrollbars to the window
    cv2.createTrackbar("x", "image", 0, img.shape[1], lambda x: None)
    cv2.createTrackbar("y", "image", 0, img.shape[0], lambda x: None)
    while True:
        # update the clone image with the current scrollbar positions
        x_pos = cv2.getTrackbarPos("x", "image")
        y_pos = cv2.getTrackbarPos("y", "image")
        clone = img[y_pos:y_pos+img.shape[0], x_pos:x_pos+img.shape[1]].copy()
        cv2.imshow("image", clone)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            clone = img.copy()
        elif key == ord("c"):
            break
    if len(ref_point) == 2:
        crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]

        crop_img = cv2.resize(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB), (484, 135))
        crop_img[np.all(crop_img == [0, 255, 0], axis=-1)] = rect_color

        mainpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Signatures/temp/LineSweep_Results")
        if not os.path.exists(mainpath):
            os.makedirs(mainpath)
        path = os.path.join(mainpath, "LineSweep_Results_" + name)
        if not os.path.exists(path):
            os.makedirs(path)
        s2 = "LineSweep_Results_" + image_name
        cv2.imwrite(os.path.join(path, s2), crop_img)
        cv2.destroyAllWindows()

def deteccion(name, opcion, user):
    global s2

    images_dir = f"../uploads/Users/{user}/Signatures/temp/OCR_Results/OCR_Results_"+name
    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), images_dir
    )

    if not os.path.exists(input_path) or len(os.listdir(input_path)) == 0:
        # call crop_images_in_directory if OCR_Results folder is empty or doesn't exist
        for filename in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../media/images/{name}")):
            crop_images_in_directory(f"../media/images/{name}", filename, user, name)
    else:
        # check if all the images have corresponding cropped images
        for filenameori in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../media/images/{name}")):
            for filename in os.listdir(input_path):
                cropped_filename = filename.replace("OCR_Result_", "")
                if cropped_filename not in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../media/images/{name}")):
                    crop_images_in_directory(f"../media/images/{name}", filenameori, user, name)
                else:
                    try:
                        total_files = 0
                        processed_files = 0

                        fileSize = os.stat(os.path.join(input_path, filename)).st_size
                        total_files = total_files + 1
                        if fileSize != 0:
                            processed_files = processed_files + 1
                            print("Processing " + filename)
                            img = Image.open(os.path.join(input_path,filename))
                            temp = np.array(img)

                            grayscale = img.convert("L")
                            xtra, thresh = cv2.threshold(np.array(grayscale), 128, 255, cv2.THRESH_BINARY_INV)

                            rows = thresh.shape[0]
                            cols = thresh.shape[1]

                            flagx = 0
                            indexStartX = 0
                            indexEndX = 0

                            for i in range(rows):
                                line = thresh[i, :]

                                if flagx == 0:
                                    ele = [255]
                                    mask = np.isin(ele, line)

                                    if True in mask:
                                        indexStartX = i
                                        flagx = 1

                                elif flagx == 1:
                                    ele = [255]
                                    mask = np.isin(ele, line)

                                    if True in mask:
                                        indexEndX = i

                                    elif indexStartX + 5 > indexEndX:
                                        indexStartX = 0
                                        flagx = 0
                                    else:
                                        break

                            flagy = 0
                            indexStartY = 0
                            indexEndY = 0

                            for j in range(cols):
                                line = thresh[indexStartX:indexEndX, j : j + 20]

                                if flagy == 0:
                                    ele = [255]
                                    mask = np.isin(ele, line)

                                    if True in mask:
                                        indexStartY = j
                                        flagy = 1

                                elif flagy == 1:
                                    ele = [255]
                                    mask = np.isin(ele, line)

                                    if True in mask:
                                        indexEndY = j
                                    elif indexStartY + 20 > indexEndY:
                                        indexStartY = 0
                                        flagy = 0
                                    else:
                                        break

                            cv2.line(thresh,(indexStartY, indexStartX),(indexEndY, indexStartX),(255, 0, 0),1,)

                            cv2.line(thresh,(indexStartY, indexEndX),(indexEndY, indexEndX),(255, 0, 0),1,)

                            cv2.line(thresh,(indexStartY, indexStartX),(indexStartY, indexEndX),(255, 0, 0),1,)

                            cv2.line(thresh,(indexEndY, indexStartX),(indexEndY, indexEndX),(255, 0, 0),1,)

                            if opcion == 'firma':
                                temp_np = temp[
                                          indexStartX + 345: indexEndX + 1, indexStartY: indexEndY - 100
                                          ]
                                mainpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Signatures/temp/LineSweep_Results")
                                if not os.path.exists(mainpath):
                                    os.makedirs(mainpath)
                                path = os.path.join(mainpath, "LineSweep_Results_"+name)
                                if not os.path.exists(path):
                                    os.makedirs(path)

                                s2 = "LineSweep_Result_" + filename
                                cv2.imwrite(os.path.join(path, s2), temp_np)

                            if opcion == 'firma' and name.lower().__contains__(".pdf"):
                                temp_np = temp[
                                          indexStartX + 400: indexEndX - 30, indexStartY + 70: indexEndY - 70
                                          ]
                                mainpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Signatures/temp/LineSweep_Results")
                                if not os.path.exists(mainpath):
                                    os.makedirs(mainpath)
                                path = os.path.join(mainpath, "LineSweep_Results_"+name)
                                if not os.path.exists(path):
                                    os.makedirs(path)

                                s2 = "LineSweep_Result_" + filename
                                cv2.imwrite(os.path.join(path, s2), temp_np)

                    except Exception as e:
                        crop_images_in_directory(f"../media/images/{name}", filename, user, name)

        print(str(processed_files) + "/" + str(total_files) + " files processed successfully")
        print("Processing Complete.")
        print("You may check the Result folder in the same directory to see the cropped Project_Images.")


def cleaner(name, user):
    global s3
    images_dir = f"../uploads/Users/{user}/Signatures/temp/LineSweep_Results/LineSweep_Results_"+name

    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), images_dir
    )

    total_files = 0
    processed_files = 0

    for filename in os.listdir(input_path):
        fileSize = os.stat(os.path.join(input_path, filename)).st_size
        total_files = total_files + 1
        if fileSize != 0:
            processed_files = processed_files + 1
            print("Extracting " + filename)
            # los parámetros se utilizan para eliminar los píxeles conectados de tamaño pequeño.
            constant_parameter_1 = 84
            constant_parameter_2 = 250
            constant_parameter_3 = 100

            # el parámetro se usa para eliminar los píxeles conectados de gran tamaño.
            constant_parameter_4 = 18

            # leer la imagen de entrada
            img = cv2.imread(os.path.join(input_path, filename),0)
            img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # asegurar binario

            # análisis de componentes conectados por scikit-learn frameworkk
            blobs = img > img.mean()

            blobs_labels = measure.label(blobs, background=1)
            image_label_overlay = label2rgb(blobs_labels, image=img)

            fig, ax = plt.subplots(figsize=(10, 6))

            the_biggest_component = 0
            total_area = 0
            counter = 0
            average = 0.0
            for region in regionprops(blobs_labels):
                if (region.area > 10):
                    total_area = total_area + region.area
                    counter = counter + 1
                # print region.area # (para depuración)
                # tomar regiones con áreas lo suficientemente grandes
                if (region.area >= 250):
                    if (region.area > the_biggest_component):
                        the_biggest_component = region.area

            average = (total_area/counter)
            print("the_biggest_component: " + str(the_biggest_component))
            print("average: " + str(average))

            # cálculo de proporción basado en experimentos, modifíquelo para sus casos
            # a4_small_size_outliar_constant se usa como un valor de umbral para eliminar los píxeles conectados a outliar conectados
            # son más pequeños que a4_small_size_outliar_constant para documentos escaneados de tamaño A4
            a4_small_size_outliar_constant = ((average/constant_parameter_1)*constant_parameter_2)+constant_parameter_3
            print("a4_small_size_outliar_constant: " + str(a4_small_size_outliar_constant))

            # cálculo de proporción basado en experimentos, modifíquelo para sus casos
            # a4_big_size_outliar_constant se usa como un valor de umbral para eliminar píxeles conectados extraños
            # son más grandes que a4_big_size_outliar_constant para documentos escaneados de tamaño A4
            a4_big_size_outliar_constant = a4_small_size_outliar_constant*constant_parameter_4
            print("a4_big_size_outliar_constant: " + str(a4_big_size_outliar_constant))

            # eliminar los píxeles conectados que son más pequeños que a4_small_size_outliar_constant
            pre_version = morphology.remove_small_objects(blobs_labels, a4_small_size_outliar_constant)

            # elimina los píxeles conectados que son más grandes que el umbral a4_big_size_outliar_constant
            # para deshacerse de los píxeles conectados no deseados, como los encabezados de las tablas, etc.
            component_sizes = np.bincount(pre_version.ravel())
            too_small = component_sizes > (a4_big_size_outliar_constant)
            too_small_mask = too_small[pre_version]
            pre_version[too_small_mask] = 0

            # guardar
            mainpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Signatures/temp/Cleaned_Results")
            if not os.path.exists(mainpath):
                os.makedirs(mainpath)
            path = os.path.join(mainpath, "Cleaned_Results_"+name)
            if not os.path.exists(path):
                os.makedirs(path)

            s3 = "Cleaned_Results_" + filename
            cv2.imwrite(os.path.join(path, s3), img)
            mainpath2 = f"../media/Users/{user}/Signatures/temp/Cleaned_Results"
            if not os.path.exists(mainpath2):
                os.makedirs(mainpath2)
            path2 = os.path.join(mainpath2, "Cleaned_Results_"+name)
            if not os.path.exists(path2):
                os.makedirs(path2)

            cv2.imwrite(os.path.join(path2, s3), img)

def convertImage(name, type, user, person):
    # leer las imagenes
    images_dir = "../media/"
    pop_dir = "../poppler-0.68.0/bin"
    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), images_dir
    )
    for filename in os.listdir(input_path):
        direc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../poppler-0.68.0/bin")
        print(direc)
        img = convert_from_path(os.path.join(input_path, name),500,poppler_path=r""+direc)
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../media/images")
        for i, page in enumerate(img):
            # Call the extract_check() function if the type is 'firma'
            if type == 'firma':
                # Open the image as a numpy array
                img_arr = np.array(page)
                # Call the extract_check() function with the numpy array as argument
                check_img = extract_check(img_arr)
                if check_img:
                    # Save the check image instead of the page
                    page = check_img
                else:
                    # If the check image was not found, skip the page
                    if not os.path.exists(os.path.join(path, name)):
                        os.makedirs(os.path.join(path, name))

                    page.save(os.path.join(path, name, '{}_{}.jpg'.format(name, i)), 'JPEG')

            if not os.path.exists(os.path.join(path, name)):
                os.makedirs(os.path.join(path, name))

            page.save(os.path.join(path, name, '{}_{}.jpg'.format(name, i)), 'JPEG')


        return img[0]

def preprocess_image(image):
    # Apply thresholding to remove noise and improve image quality
    threshold_value = 180
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def train_model(user, person) -> np.ndarray:
    # Get list of signature image file names from training folder
    signatures_dir = f"Users/{user}/Signatures/People/{person}"
    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), signatures_dir
    )

    signatures_files = os.listdir(input_path)

    # Load signature images and preprocess them to improve image quality
    signatures = []
    for file_name in signatures_files:
        image_path = os.path.join(input_path, file_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.bitwise_not(image)
        preprocessed_image = preprocess_image(image)
        signatures.append(preprocessed_image)

    # Check if signatures list is empty
    if not signatures:
        return None

    # Convert signatures to numpy array and normalize pixel values
    signatures = np.array(signatures) / 255.0

    # Compute mean signature image as model
    model = np.mean(signatures, axis=0)

    return model


def calculate_similarity(user, folder2_path, model: np.ndarray) -> float:
    # Get list of signature image file names from comparison folder
    signatures_dir = f"../uploads/Users/{user}/Signatures/temp/Cleaned_Results/Cleaned_Results_{folder2_path}"
    input_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), signatures_dir
    )
    signatures_files = os.listdir(input_path)

    # Load signature images and preprocess them to improve image quality
    signatures = []
    for file_name in signatures_files:
        image_path = os.path.join(input_path, file_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.bitwise_not(image)
        preprocessed_image = preprocess_image(image)
        signatures.append(preprocessed_image)

    # Check if signatures list is empty
    if not signatures:
        return 0.0

    # Convert signatures to numpy array and normalize pixel values
    signatures = np.array(signatures) / 255.0

    # Compute mean signature image as comparison
    try:
        comparison = np.mean(signatures, axis=0)
    except ValueError:
        return 0.0 # Return 0 if signatures is empty or has incompatible dimensions

    # Compute cosine similarity between model and comparison
    try:
        similarity = cosine_similarity(model.reshape(1, -1), comparison.reshape(1, -1))[0][0]
    except ValueError:
        return 0.0 # Return 0 if model and comparison have incompatible dimensions

    return similarity

def evaluate_similarity(user, person, folder2_path) -> float:
    # Train model on signature images for person
    model = train_model(user, person)

    # Calculate similarity between model and signatures in folder2_path
    similarity = calculate_similarity(user, folder2_path, model)

    print("SIMILARITY: ", similarity)

    return similarity * 100

def add_cleaned_results_to_signatures(user, person, name):
    # Check if the signatures directory for the person exists, create it if it doesn't
    signatures_dir = f"Users/{user}/Signatures/People/{person}"
    path3 = f"../media/Users/{user}/Signatures/People/{person}"

    signatures_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), signatures_dir
    )

    input_path3 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), path3
    )

    if not os.path.exists(signatures_path):
        os.makedirs(signatures_path)

    if not os.path.exists(input_path3):
        os.makedirs(input_path3)

    # Copy all images from the cleaned results directory to the signatures directory
    cleaned_results_dir = f"Users/{user}/Signatures/temp/Cleaned_Results/Cleaned_Results_{name}"
    cleaned_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), cleaned_results_dir
    )

    if not os.path.exists(cleaned_path):
        print(f"Cleaned results directory {cleaned_path} does not exist. Aborting.")
        return

    for filename in os.listdir(cleaned_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            shutil.copy(os.path.join(cleaned_path, filename), signatures_path)
            shutil.copy(os.path.join(cleaned_path, filename), input_path3)

    print(f"All cleaned results for {name} have been added to the signatures directory for {person}.")
def matchAdd(folder1_path, user, person):
    path1 = f'../uploads/Users/{user}/Signatures/temp/Cleaned_Results/Cleaned_Results_{folder1_path}'
    path2 = f"Users/{user}/Signatures/People/{person}"
    path3 = f"../media/Users/{user}/Signatures/People/{person}"


    # Construct the full paths to the folders
    input_path1 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), path1
    )

    input_path2 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), path2
    )

    input_path3 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), path3
    )

    if not os.path.exists(input_path2):
        os.makedirs(input_path2)

    if not os.path.exists(input_path3):
        os.makedirs(input_path3)

    # Determine which folder has more images
    more_images_path = input_path3
    more_images_path2 = input_path1

    # Load the images from the more images folder
    more_images = []
    for filename in os.listdir(more_images_path):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(more_images_path, filename), cv2.IMREAD_GRAYSCALE)
            more_images.append(img)

    # Load the images from the more images folder
    more_images2 = []
    for filename in os.listdir(more_images_path2):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(more_images_path2, filename), cv2.IMREAD_GRAYSCALE)
            more_images2.append(img)

    # Load the images from the path3 folder and calculate similarity
    num_similar = 0
    for filename in os.listdir(input_path3):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(input_path3, filename), cv2.IMREAD_GRAYSCALE)
            for ref_img in more_images2:
                similarity = cv2.matchTemplate(img, ref_img, cv2.TM_CCOEFF_NORMED)
                if similarity > 0.9:
                    num_similar += 1
                    break

    # Load the images from the path3 folder and calculate similarity
    non_similar_images = []
    for filename in os.listdir(input_path1):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(input_path1, filename), cv2.IMREAD_GRAYSCALE)
            similar = False
            for ref_img in more_images:
                similarity = cv2.matchTemplate(img, ref_img, cv2.TM_CCOEFF_NORMED)
                if similarity > 0.9:
                    similar = True
                    break
            if num_similar < 5:
                non_similar_images.append(filename)
            else:
                if not similar:
                    non_similar_images.append(filename)

    # Copy non-similar images to path3
    for filename in non_similar_images:
        shutil.copyfile(os.path.join(input_path1, filename), os.path.join(input_path2, filename))
        shutil.copyfile(os.path.join(input_path1, filename), os.path.join(input_path3, filename))

    # Delete extra similar images
    similar_images = []
    for filename in os.listdir(input_path3):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(input_path3, filename), cv2.IMREAD_GRAYSCALE)
            for ref_img in more_images2:
                similarity = cv2.matchTemplate(img, ref_img, cv2.TM_CCOEFF_NORMED)
                if similarity > 0.9:
                    similar_images.append(filename)
                    break
    if len(similar_images) > 5:
        for filename in similar_images[5:]:
            os.remove(os.path.join(input_path3, filename))
            os.remove(os.path.join(input_path2, filename))

    # Calculate the percentage of similarity
    percentage_similarity = (1 - (len(non_similar_images) / float(len(os.listdir(input_path3))))) * 100.0

    return percentage_similarity


def extract_check(img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Convert image to grayscale and binarize
    gray = 0.2989 * img[:,:,0] + 0.5870 * img[:,:,1] + 0.1140 * img[:,:,2]
    thresh = (gray < 200).astype(int) * 255

    # Find check region using connected components
    labels = measure.label(thresh)
    regions = measure.regionprops(labels)
    check_region = None
    for props in regions:
        y1, x1, y2, x2 = props.bbox
        width = x2 - x1
        height = y2 - y1
        if width > 100 and height > 50 and width / height > 1.5 and width / height < 3:
            check_region = (x1, y1, x2, y2)
            break

    # Extract check image and check if it's from a target bank
    if check_region:
        check_img = Image.fromarray(img[check_region[1]:check_region[3], check_region[0]:check_region[2]])
        check_text = pytesseract.image_to_string(check_img)
        # Define regular expressions to match each bank's name
        banreservas_regex = re.compile(r"ban\s*reservas", re.IGNORECASE)
        popular_regex = re.compile(r"popular", re.IGNORECASE)
        bhd_regex = re.compile(r"bhd", re.IGNORECASE)
        scotiabank_regex = re.compile(r"scotiabank", re.IGNORECASE)
        contrato_regex = re.compile(r"contrato", re.IGNORECASE)
        contratacion_regex = re.compile(r"contratacion", re.IGNORECASE)

        if banreservas_regex.search(check_text) or popular_regex.search(check_text) or bhd_regex.search(check_text) or scotiabank_regex.search(check_text):
            return check_img
        else:
            return False

    return False