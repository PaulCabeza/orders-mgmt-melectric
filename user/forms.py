from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.core.exceptions import ValidationError

class MyCustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']    
    
    # def clean_email(self):
    #     # email = email
    #     email = self.cleaned_data['email']
    #     # email = self.email
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError('Email Already Exists')
    #     return email