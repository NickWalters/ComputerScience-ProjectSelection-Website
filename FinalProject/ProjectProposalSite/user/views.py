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
            Organisation = userform.cleaned_data.get('Organisation')
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
                                            Organisation=Organisation
                                             )
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        userform = UserForm()
    return render(request, 'users/user_registration_form.html', {'user_form': userform})


@login_required(login_url='/login/')
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    userprofile = User.objects.get(pk=profile.user_id)
    context = {'profile': profile,
               'userprofile': userprofile}
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='/login/')
def update_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():            
            form.save()
        messages.success(request, f'Profile has been updated!')    
        return redirect('profile', pk=pk)
    else:
        form = UpdateForm(instance=profile)
    return render(request, 'users/user_update_form.html', context={'form': form})

@login_required(login_url='/login/')
def user_list(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=False)
        context = {
            'users': users
        }
        return render(request, 'users/user_list.html', context=context)
    return redirect('home-page')