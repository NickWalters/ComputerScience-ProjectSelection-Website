from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from user.user_form import UserForm, UpdateForm
from user.models import Profile
from django.contrib.auth.models import User


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
            Company_Name = userform.cleaned_data.get('Company_Name')
            Company_Business = userform.cleaned_data.get('Company_Business')
            messages.success(request, f'Account created {UserName}! Please wait for admin to active your account')

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
                                            Company_Name=Company_Name,
                                            Company_Business=Company_Business
                                             )
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        userform = UserForm()
    return render(request, 'users/user_registration_form.html', {'user_form': userform})

@login_required(login_url='/login/')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='/login/')
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():            
            form.save()
        messages.success(request, f'Profile has been updated!')    
        return redirect('profile')
    else:
        form = UpdateForm(instance=profile)
    return render(request, 'users/user_update_form.html', context={'form': form})
