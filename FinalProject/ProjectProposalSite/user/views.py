from django.shortcuts import render, redirect
from django.contrib import messages
from user.user_form import UserForm
from user.models import Profile


def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid() :
            UserName = userform.cleaned_data.get('username')
            First_Name = userform.cleaned_data.get('First_Name')
            Last_Name = userform.cleaned_data.get('Last_Name')
            Email = userform.cleaned_data.get('Email')
            Phone = userform.cleaned_data.get('Phone')
            Company_Name = userform.cleaned_data.get('Company_Name')
            Company_Business = userform.cleaned_data.get('Company_Business')
            messages.success(request, f'Accoount created {UserName}!')

            profile = Profile.objects.create(
                                            username=UserName,
                                            First_Name=First_Name,
                                            Last_Name=Last_Name,
                                            Email=Email,
                                            Phone=Phone,
                                            Company_Name=Company_Name,
                                            Company_Business=Company_Business
                                             )
            profile.save()
            userform.save()

            return redirect('login')
    else:
        userform = UserForm()
    return render(request, 'users/user_registration_form.html', {'user_form': userform})
