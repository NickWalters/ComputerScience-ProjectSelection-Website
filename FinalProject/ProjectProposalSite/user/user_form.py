from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Form used when creating a new user
class UserForm(UserCreationForm):
    First_Name = forms.CharField(max_length=20)
    Last_Name = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=120)
    Phone = forms.RegexField(regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', max_length=20)
    Organisation = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username',
                  'First_Name',
                  'Last_Name',
                  'Email',
                  'password1',
                  'password2',
                  'Phone',
                  'Organisation'
                  )

# Form used when creating a new user
class UpdateForm(forms.ModelForm):
    First_Name = forms.CharField(max_length=20)
    Last_Name = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=120)
    Phone = forms.RegexField(regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', max_length=20)
    Organisation = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('First_Name',
                  'Last_Name',
                  'Email',
                  'Phone',
                  'Organisation'
                  )


class PasswordChange(UserCreationForm):
    class Meta:
        model = User
        fields = ('password1',
                  'password2'
                  )