from django.db import models

# Create your models here.
from django.db import models
import MySQLdb as Database
from django.forms import ModelForm, Textarea
from django.db import models 
# Create your models here.

class RegisteredForms(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)
    password=models.CharField(max_length=100)