import os

from django import forms

from .models import Upload
#from .models import OCR_Result
class MyModelForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['documento']

"""
    class Metas:
        model = OCR_Result
        fields = ['documento']
"""