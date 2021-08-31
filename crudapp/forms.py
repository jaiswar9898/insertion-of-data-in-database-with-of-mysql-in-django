from django import forms 
from crudapp.models import RegisteredForms
from django.forms import ModelForm, Textarea

class FormRegisterForm(forms.ModelForm):
    class Meta:
        model=RegisteredForms
        fields=["username","email","phone_number","password"]