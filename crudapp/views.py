from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect 
from crudapp.forms import FormRegisterForm
from crudapp.models import RegisteredForms


def Register(request):
    form = FormRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={'FormRegisterForm':FormRegisterForm}
    return render(request,'register.html',context)

def home(request):
    blog=RegisteredForms.objects.all()
    print(blog)
    return render(request,'home.html',{'blogs':blog})


