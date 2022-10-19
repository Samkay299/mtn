from django import forms
from django.forms import ModelForm
from .models import Applicant

class ApplicantForm(ModelForm):
    class Meta:
        model=Applicant
        fields=( 'name', 'address', 'zip_code','phone','web','Email_address', 'gender')
        labels ={
            'name': '',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'Email_address':'',
            # 'gender':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip_code'}),
            'phone':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'web_address'}),
            'Email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'abc@email.com'}),
            # 'gender': forms.TextInput(attrs={'class': 'form-control'}),
        }
    