import time

from django.contrib.auth.models import User
from django.db import models

from .utils import cleaner, OCR, deteccion, convertImage, matchAdd, evaluate_similarity, \
    add_cleaned_results_to_signatures
from .utiles import extract_letters, classify_letters, calculate_similarity, compare_folders
from PIL import Image
from io import BytesIO
import numpy as np
from django.core.files.base import ContentFile
import os
from datetime import datetime

from django.conf import settings

DOCUMENTS_CHOICES = (
    ('firma', 'FIRMA'),
    ('texto','TEXTO'),
    ('otro', 'OTRO CHEQUE'),
)
# TODO add contour detection for enhanced accuracy
extraida1 = ''
extraida2 = ''

# Create your models here.

class Upload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) # replace 1 with the ID of the default user

    word = models.CharField(max_length=100, blank=True, null=True)

    documento = models.CharField(max_length=50, choices=DOCUMENTS_CHOICES, default='firma')

    image1 = models.ImageField(upload_to='images', null=True)

    image2 = models.ImageField(upload_to='images', null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        global extraida1, accuracy
        global extraida2
        typeo = self.documento

        if self.image1.name is not None:
            # Store Pdf with convert_from_path function
            convertImage(self.image1.name, typeo, self.user, self.word)

            # Save all the pages of document 1 as separate images
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../media/images", self.image1.name)
            extraida1 = self.image1.name
            for filename in os.listdir(path):
                pil_image1 = Image.open(os.path.join(path, filename))
                cv_img1 = np.array(pil_image1)
                im_pil = Image.fromarray(cv_img1)
                name1 = self.image1.name + '_' + filename
                buffer = BytesIO()
                im_pil.save(buffer, format='png')
                image_png = buffer.getvalue()
                self.image1.save(name1, ContentFile(image_png), save=False)
                self.image1.save(str(self.image1), ContentFile(image_png), save=False)

        if self.image2.name is not None:
            # Store Pdf with convert_from_path function
            convertImage(self.image2.name, typeo, self.user, self.word)

            # Save all the pages of document 2 as separate images
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../media/images", self.image2.name)
            extraida2 = self.image2.name
            for filename in os.listdir(path):
                pil_image2 = Image.open(os.path.join(path, filename))
                cv_img2 = np.array(pil_image2)
                im_pil2 = Image.fromarray(cv_img2)
                name2 = self.image2.name + '_' + filename
                buffer2 = BytesIO()
                im_pil2.save(buffer2, format='png')
                image_png2 = buffer2.getvalue()
                self.image2.save(name2, ContentFile(image_png2), save=False)
                self.image2.save(str(self.image2), ContentFile(image_png2), save=False)

        super().save(*args, **kwargs)

        if typeo == 'texto':
            if self.image1.name is not None and self.image2.name is not None:
                now = datetime.now()
                timestamp = now.strftime("%d%m%Y%H%M%S") + self.word
                extract_letters(extraida1, extraida2, timestamp, self.user)
                classify_letters(timestamp, self.user, self.word)
                #calculate_similarity(timestamp, self.user)
                accuracy = compare_folders(self.user, self.word, timestamp)

            if self.image1.name is None and self.image2.name is not None:
                now = datetime.now()
                timestamp = now.strftime("%d%m%Y%H%M%S") + self.word
                extract_letters(extraida1, extraida2, timestamp, self.user)
                classify_letters(timestamp, self.user, self.word)
                #calculate_similarity(timestamp, self.user)
                accuracy = compare_folders(self.user, self.word, timestamp)

            if self.image2.name is None and self.image1.name is not None:
                now = datetime.now()
                timestamp = now.strftime("%d%m%Y%H%M%S") + self.word
                extract_letters(extraida1, extraida2, timestamp, self.user)
                classify_letters(timestamp, self.user, self.word)
                #calculate_similarity(timestamp, self.user)
                accuracy = 100

            return accuracy
        if typeo == 'firma':
            if self.image1.name is not None and self.image2.name is not None:
                try:
                    OCR(extraida1, typeo, self.user)
                except:
                    pass # do nothing if OCR() raises an exception
                deteccion(extraida1, typeo, self.user)
                cleaner(extraida1,self.user)
                try:
                    OCR(extraida2, typeo, self.user)
                except:
                    pass # do nothing if OCR() raises an exception
                deteccion(extraida2,typeo, self.user)
                cleaner(extraida2,self.user)
                add_cleaned_results_to_signatures(self.user, self.word, extraida1)

                accuracy = evaluate_similarity(self.user, self.word, extraida2)

            if self.image1.name is None and self.image2.name is not None:
                try:
                    OCR(extraida2, typeo, self.user)
                except:
                    pass # do nothing if OCR() raises an exception
                deteccion(extraida2,typeo, self.user)
                cleaner(extraida2,self.user)
                accuracy = evaluate_similarity(self.user, self.word, extraida2)

            if self.image2.name is None and self.image1.name is not None:
                try:
                    OCR(extraida1, typeo, self.user)
                except:
                    pass # do nothing if OCR() raises an exception
                deteccion(extraida1, typeo, self.user)
                cleaner(extraida1,self.user)
                add_cleaned_results_to_signatures(self.user, self.word, extraida1)
                accuracy = 100


            return accuracy