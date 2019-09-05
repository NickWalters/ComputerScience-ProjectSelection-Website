from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProjectProposalForm

# home page
def home(request):
    return render(request, 'home.html')


# # Sign in page
# def sign_in(request):
#     return render(request, 'signin.html')
#
#
# # user registration part
# def user_register(request):
#     return render(request, 'user_registration_form.html')

# project registration form

def project_registration(request):
    if request.method == 'POST':
        form = ProjectProposalForm(request.POST)
        if form.is_valid():
            #form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Project Proposal Named {title} was created!')
            return redirect('home-page')
    else:
        form = ProjectProposalForm()
    return render(request, 'project_registration.html', {'form':form})
