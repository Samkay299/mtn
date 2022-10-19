from django.shortcuts import render
from .models import Applicant
from .forms import ApplicantForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'examapp/index.html')

def about(request):
    return render(request, 'examapp/about.html')

def contact(request):
    return render(request, 'examapp/contact.html')

def register(request):
    submitted = False
    if request.method=="POST":
        form=ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form=ApplicantForm
        if 'submitted' in request.GET:
            submitted =True
    return render(request,'examapp/register.html',{'form': form,'submitted': submitted})
def register_user(request):
    return render(request, 'authenticate/signup.html', {})