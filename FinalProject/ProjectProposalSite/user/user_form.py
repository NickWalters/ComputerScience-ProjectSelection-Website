from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_registration_form(UserCreationForm):
    First_Name = forms.CharField(max_length=20)
    Last_Name = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=120)
    Phone = forms.IntegerField()
    Company_Name = forms.CharField(max_length=100)
    Company_Business = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['First_Name', 'Last_Name', 'Email',  'password1', 'password2', 'Phone', 'Company_Name', 'Company_Business']
