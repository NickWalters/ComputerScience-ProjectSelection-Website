from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user.forms import UserForm, UpdateForm, PasswordChange
from user.models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# User registration: collect data from forms, save into User model and Profile model
def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():

            # Get post data
            UserName = userform.cleaned_data.get('username')
            First_Name = userform.cleaned_data.get('First_Name')
            Last_Name = userform.cleaned_data.get('Last_Name')
            Password = userform.cleaned_data.get('password2')
            Email = userform.cleaned_data.get('Email')
            Phone = userform.cleaned_data.get('Phone')
            Organisation = userform.cleaned_data.get('Organisation')
            messages.success(request, f'Account created {UserName}! Please wait for admin to activate your account')

            # Save data into user model
            user = User.objects.create_user(
                                            username=UserName,
                                            password=Password,
                                            first_name=First_Name,
                                            last_name=Last_Name,
                                            email=Email
                                        )
            user.is_active = False
            user.save()

            # Save data into profile
            profile = Profile.objects.create(
                                            # user=UserName,
                                            user_id=int(user.id),
                                            First_Name=First_Name,
                                            Last_Name=Last_Name,
                                            Email=Email,
                                            Phone=Phone,
                                            Organisation=Organisation
                                             )
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        userform = UserForm()
    return render(request, 'users/user_registration_form.html', {'user_form': userform})

#View profile function
@login_required(login_url='/login/')
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    userPK = pk
    userprofile = User.objects.get(pk=profile.user_id)
    
    userName = request.user.username
    strUser = str(userName)
    strSupervisor = str(profile.user)    
    # Check if the user has permission to view another profile
    if strSupervisor != strUser:
        if not request.user.is_superuser:
            return render(request, 'denied.html')

    context = {'profile': profile,
               'userprofile': userprofile,
               'userPK': userPK}
    return render(request, 'users/user_profile.html', context)

#Update function for profiles
@login_required(login_url='/login/')
def update_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    userobject = User.objects.get(pk=profile.user_id)

    user = request.user.username
    strUser = str(user)
    strSupervisor = str(profile.user)    
    # Check if the user trying to update profile has permission
    if strSupervisor != strUser:
        if request.user.is_superuser:
            return render(request, 'denied.html')

    form = UpdateForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():            
            form.save()
            userobject.first_name = form.cleaned_data['First_Name']
            userobject.last_name = form.cleaned_data['Last_Name']
            userobject.email = form.cleaned_data['Email']
            userobject.save()
        messages.success(request, f'Profile has been updated!')    
        return redirect('profile', pk=pk)
    else:
        form = UpdateForm(instance=profile)
    return render(request, 'users/user_update_form.html', context={'form': form})

#Update password from profile
@login_required(login_url='/login/')
def password_change(request, pk):
    profile = Profile.objects.get(pk=pk)
    user = User.objects.get(pk=profile.user_id)
    form = PasswordChange(request.POST, instance=user)

    username = request.user.username
    strUser = str(username)
    strSupervisor = str(profile.username)    
    # Check if the user trying to update password
    # is the correct user
    if strSupervisor != strUser:
        if request.user.is_superuser:
            return render(request, 'denied.html')



    if request.method == 'POST':
        if form.is_valid():
            new_password = form.cleaned_data.get('password1')
            user.set_password(new_password)
            form.save()
            messages.success(request, f'Password has been updated!')
            return redirect('profile', pk=pk)
        else:
            form = PasswordChange(request.POST)
            return render(request, 'users/user_changepassword_form.html', context={'form': form})
    else:
        form = PasswordChange()
    return render(request, 'users/user_changepassword_form.html', context={'form': form})

#Admin view of user list
@login_required(login_url='/login/')
def user_list(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=False)
        context = {
            'users': users,
        }
        return render(request, 'users/user_list.html', context=context)
    else:
        return render(request, 'denied.html')
    return redirect('home-page')

#Approve the user or not
@login_required(login_url='/login/')
def approve_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if not request.user.is_superuser:
        return render(request, 'denied.html')
    user.is_active = True
    user.save()
    send_mail('Your account has been approved for the UWA Project Proposal Site', f'Account for {user.first_name} {user.last_name} with the username {user.username} has just been approved!\n'
                                                                                  f'You can now login at: http://127.0.0.1:8000/login/', settings.EMAIL_HOST_USER, [user.email])
    return redirect('home-page')

#Delete users from user list
@login_required(login_url='/login/')
def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    profile = Profile.objects.get(user_id=pk)
    if not request.user.is_superuser:
        return render(request, 'denied.html')
    user.delete()
    profile.delete()
    return redirect('home-page')
