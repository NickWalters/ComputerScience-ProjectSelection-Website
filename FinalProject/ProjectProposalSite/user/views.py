from django.shortcuts import render, redirect
from django.contrib import messages
from FinalProject.ProjectProposalSite.user.user_form import User_registration_form


def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            #form.save()
            firstname = form.cleaned_data.get('First_Name')
            lastname = form.cleaned_data.get('Last_Name')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Accoount created for {lastname, firstname, password}!')
            return redirect('home-page')
    else:
        form = User_registration_form()
    return render(request, 'users/user_registration_form.html', {'form': form})
