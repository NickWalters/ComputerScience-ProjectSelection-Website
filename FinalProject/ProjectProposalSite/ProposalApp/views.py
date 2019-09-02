from django.shortcuts import render


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
    form = ProjectProposalForm()
    return render(request, 'project_registration.html', {'form':form})
