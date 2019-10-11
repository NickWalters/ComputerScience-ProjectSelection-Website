from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Form used when creating a new user
class UserForm(UserCreationForm):
    First_Name = forms.CharField(max_length=20)
    Last_Name = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=120)
    Phone = forms.IntegerField()
    Organisation_Name = forms.CharField(max_length=100)
    Organisation_Business = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username',
                  'First_Name',
                  'Last_Name',
                  'Email',
                  'password1',
                  'password2',
                  'Phone',
                  'Organisation_Name',
                  'Organisation_Business'
                  )

# Form used when creating a new user
class UpdateForm(forms.ModelForm):
    First_Name = forms.CharField(max_length=20)
    Last_Name = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=120)
    Phone = forms.IntegerField()
    Organisation_Name = forms.CharField(max_length=100)
    Organisation_Business = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('First_Name',
                  'Last_Name',
                  'Email',
                  'Phone',
                  'Organisation_Name',
                  'Organisation_Business'
                  )