from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    input_excel = forms.FileField()



 