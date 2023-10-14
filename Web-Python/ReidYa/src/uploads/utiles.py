import cv2
import numpy as np
import os

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from skimage.feature import hog
import pytesseract
from sklearn.metrics.pairwise import cosine_similarity

def classify_letters(timestamp, user, person):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Step 1: Load images of letters from Test_Letters folder
    letter_images = []
    labels = []
    images_dir = f"../uploads/Test_Letters"  # Use ASCII value to get the corresponding letter
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), images_dir)
    for foldername in os.listdir(folder_path):
        folderpath = os.path.join(folder_path, foldername)
        if os.path.isdir(folderpath):
            for filename in os.listdir(folderpath):
                if filename.endswith(".jpg"):
                    filepath = os.path.join(folderpath, filename)
                    img = cv2.imread(filepath)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    resized = cv2.resize(gray, (28, 28))
                    _, binary = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                    letter_images.append(binary)
                    labels.append(ord(foldername) - 65)  # A=0, B=1, etc.

    # Step 2: Extract features of letter images using HOG
    hog_features = []
    for img in letter_images:
        hog_feature = hog(img, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), block_norm="L2-Hys")
        hog_features.append(hog_feature)
    X_train = np.array(hog_features)
    y_train = np.array(labels)

    # Step 3: Train SVM classifier
    svm = SVC(kernel="rbf", C=10, gamma=0.01, random_state=42)
    svm.fit(X_train, y_train)

    # Step 4: Classify extracted letters using SVM classifier and OCR
    print("-----Extracted Folder 1-----")
    extracted_folder1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/temp/Extracted_Letters_Folder1_"+ timestamp)
    if os.path.exists(extracted_folder1):
        for filename in os.listdir(extracted_folder1):
            if filename.endswith(".jpg"):
                filepath = os.path.join(extracted_folder1, filename)
                img = cv2.imread(filepath)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                resized = cv2.resize(gray, (28, 28))
                _, binary = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                hog_feature = hog(binary, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), block_norm="L2-Hys")
                prediction = svm.predict([hog_feature])[0]
                letter = chr(prediction + 65) # Convert label back to letter
                ocr_letter = pytesseract.image_to_string(binary, config='--psm 10')

                result_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/temp/Classified_Letters_Extracted1_{timestamp}/{letter}")
                if not os.path.exists(result_folder):
                    os.makedirs(result_folder)
                result_filepath = os.path.join(result_folder, filename)
                cv2.imwrite(result_filepath, binary)

                result_folder2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/People/{person}/Classified_Letters/{letter}")
                if not os.path.exists(result_folder2):
                    os.makedirs(result_folder2)
                result_filepath2 = os.path.join(result_folder2, filename)
                cv2.imwrite(result_filepath2, binary)

                result_folder3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../media/Users/{user}/Texts/People/{person}/Classified_Letters/{letter}")
                if not os.path.exists(result_folder3):
                    os.makedirs(result_folder3)
                result_filepath3 = os.path.join(result_folder3, filename)
                cv2.imwrite(result_filepath3, binary)

                if ocr_letter.isalpha() and ocr_letter.upper() == letter:
                    # If OCR recognized the same letter as the classifier, print the result
                    print(f"Extracted letter '{letter}' from '{filename}' (correctly classified by SVM and OCR)")
                else:
                    # If OCR recognized a different letter or didn't recognize anything, print the result with a warning
                    print(f"Extracted letter '{letter}' from '{filename}', but OCR recognized '{ocr_letter}' (warning)")

    print("-----Extracted Folder 2-----")
    extracted_folder2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/temp/Extracted_Letters_Folder2_" + timestamp)
    if os.path.exists(extracted_folder2):
        for filename in os.listdir(extracted_folder2):
            if filename.endswith(".jpg"):
                filepath = os.path.join(extracted_folder2, filename)
                img = cv2.imread(filepath)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                resized = cv2.resize(gray, (28, 28))
                _, binary = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                hog_feature = hog(binary, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), block_norm="L2-Hys")
                prediction = svm.predict([hog_feature])[0]
                letter = chr(prediction + 65) # Convert label back to letter
                ocr_letter = pytesseract.image_to_string(binary, config='--psm 10')
                result_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/temp/Classified_Letters_Extracted2_{timestamp}/{letter}")
                if not os.path.exists(result_folder):
                    os.makedirs(result_folder)
                result_filepath = os.path.join(result_folder, filename)
                cv2.imwrite(result_filepath, binary)
                if ocr_letter.isalpha() and ocr_letter.upper() == letter:
                    # If OCR recognized the same letter as the classifier, print the result
                    print(f"Extracted letter '{letter}' from '{filename}' (correctly classified by SVM and OCR)")
                else:
                    # If OCR recognized a different letter or didn't recognize anything, print the result with a warning
                    print(f"Extracted letter '{letter}' from '{filename}', but OCR recognized '{ocr_letter}' (warning)")

    print("Finished classifying and extracting letters")

def calculate_similarity(timestamp, user):
    images_dir = f"../uploads/Users/{user}/Texts/temp/Classified_Letters_" + timestamp
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), images_dir)
    total_similarity_sum = 0
    total_images = 0
    for foldername in os.listdir(folder_path):
        folderpath = os.path.join(folder_path, foldername)
        if os.path.isdir(folderpath):
            image_names = os.listdir(folderpath)
            image_paths = [os.path.join(folderpath, image_name) for image_name in image_names]
            num_images = len(image_paths)
            total_images += num_images
            similarity_matrix = np.zeros((num_images, num_images))

            for i in range(num_images):
                for j in range(i + 1, num_images):
                    image1 = cv2.imread(image_paths[i], cv2.IMREAD_GRAYSCALE)
                    image2 = cv2.imread(image_paths[j], cv2.IMREAD_GRAYSCALE)

                    # Resize images to match size
                    height, width = min(image1.shape[0], image2.shape[0]), min(image1.shape[1], image2.shape[1])
                    image1 = cv2.resize(image1[:height, :width], (28, 28))
                    image2 = cv2.resize(image2[:height, :width], (28, 28))

                    # Calculate difference between images
                    difference = cv2.absdiff(image1, image2)

                    # Calculate similarity percentage
                    similarity_percentage = 1 - (np.count_nonzero(difference) / difference.size)
                    similarity_matrix[i, j] = similarity_percentage
                    similarity_matrix[j, i] = similarity_percentage

            # Calculate average similarity percentage for current subfolder
            total_similarity = np.sum(similarity_matrix) - num_images  # Subtract diagonal elements
            average_similarity = total_similarity / (num_images**2 - num_images)
            total_similarity_sum += average_similarity
            #print(f"Average similarity for subfolder {foldername}: {average_similarity * 100:.2f}%")

    # Calculate total average similarity percentage for all subfolders
    total_average_similarity = total_similarity_sum / total_images
    #print(f"Total average similarity of classification: {total_average_similarity * 100:.2f}%")

def extract_letters(name1, name2, timestamp, user):

    if (name1 is not ''):
        ruta1 = "../media/images/"+name1

    else:
        ruta1 = 'not_found'

    if (name2 is not ''):
        ruta2 = "../media/images/"+name2
    else:
        ruta2 = 'not_found'

    folder1 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ruta1
    )

    folder2 = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ruta2
    )

    # Create output folders if folder1 or folder2 exists
    if os.path.exists(folder1):
        path1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/temp/Extracted_Letters_Folder1_" + timestamp)
        if not os.path.exists(path1):
            os.makedirs(path1)
    else:
        path1 = None

    if os.path.exists(folder2):
        path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Users/{user}/Texts/temp/Extracted_Letters_Folder2_" + timestamp)
        if not os.path.exists(path2):
            os.makedirs(path2)
    else:
        path2 = None

    # Process images in folder 1
    if path1 is not None:
        for filename in os.listdir(folder1):
            image_path = os.path.join(folder1, filename)
            if os.path.isfile(image_path):
                # Load the image and convert it to grayscale
                image = cv2.imread(image_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Threshold the image to get a binary image
                _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

                # Find contours of connected components in the binary image
                contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Extract each letter as an individual image
                letters = []
                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if w > 5 and h > 5:  # Exclude small contours (likely to be noise)
                        letter_image = binary[y:y+h, x:x+w]
                        letter_image = cv2.resize(letter_image, (28, 28))
                        letters.append(letter_image)

                # Save the extracted letters
                for i, letter in enumerate(letters):
                    cv2.imwrite(os.path.join(path1, f"{filename}_{i}.jpg"), letter)

    # Process images in folder 2
    if path2 is not None:
        for filename in os.listdir(folder2):
            image_path = os.path.join(folder2, filename)
            if os.path.isfile(image_path):
                # Load the image and convert it to grayscale
                image = cv2.imread(image_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Threshold the image to get a binary image
                _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

                # Find contours of connected components in the binary image
                contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Extract each letter as an individual image
                letters = []
                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if w > 5 and h > 5: # Exclude small contours (likely to be noise)
                        letter_image = binary[y:y+h, x:x+w]
                        letter_image = cv2.resize(letter_image, (28, 28))
                        letters.append(letter_image)

                # Save the extracted letters
                for i, letter in enumerate(letters):
                    cv2.imwrite(os.path.join(path2, f"{filename}_{i}.jpg"), letter)

def compare_folders(user, person, timestamp) -> float:
    base_dir = f"../uploads/Users/{user}/Texts"
    temp_dir = f"{base_dir}/temp/Classified_Letters_Extracted2_{timestamp}"
    person_dir = f"{base_dir}/People/{person}/Classified_Letters"

    base_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), base_dir
    )

    temp_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), temp_dir
    )

    person_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), person_dir
    )

    similarities = {}

    # Get a list of all folder names in the person folder
    person_folders = [f for f in os.listdir(person_folder) if os.path.isdir(os.path.join(person_folder, f))]

    for folder in person_folders:
        # Check if the current folder exists in the temporary folder
        if os.path.isdir(os.path.join(temp_folder, folder)):
            # Get the list of files in the person folder for the current folder
            person_files = os.listdir(os.path.join(person_folder, folder))
            person_images = []

            # Load each image and store it in a list
            for file in person_files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    image_path = os.path.join(person_folder, folder, file)
                    image = cv2.imread(image_path)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    image = cv2.resize(image, (64, 64))
                    person_images.append(image)

            # Get the list of files in the temporary folder for the current folder
            temp_files = os.listdir(os.path.join(temp_folder, folder))
            temp_images = []

            # Load each image and store it in a list
            for file in temp_files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    image_path = os.path.join(temp_folder, folder, file)
                    image = cv2.imread(image_path)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    image = cv2.resize(image, (64, 64))
                    temp_images.append(image)

            # Compute the similarity between the two sets of images using cosine similarity
            if len(temp_images) > 0 and len(person_images) > 0:
                temp_images = np.array(temp_images).reshape(len(temp_images), -1)
                person_images = np.array(person_images).reshape(len(person_images), -1)
                similarity = cosine_similarity(temp_images, person_images)
                max_similarity = np.max(similarity, axis=1).mean()  # Take the mean of maximum similarity values along each row
                similarities[folder] = max_similarity

    total_similarity = sum(similarities.values()) / len(similarities) if len(similarities) > 0 else 0
    print("Total Average Similarity:", total_similarity)

    # Get the list of folders in the temporary folder that do not exist in the person folder
    temp_only_folders = [f for f in os.listdir(temp_folder) if os.path.isdir(os.path.join(temp_folder, f)) and f not in person_folders]

    # Add a penalty for folders that only exist in the temporary folder
    if total_similarity < 0.81:
        for folder in temp_only_folders:
            total_similarity -= 0.1

    print("Total Average Similarity2:", total_similarity)
    return total_similarity * 100