from django.shortcuts import render


def home(request):
    return render(request, 'undergraduate_list/home.html')


def registration(request):
    return render(request, 'undergraduate_list/registration_form.html')


def index(request):
    return render(request, 'undergraduate_list/index.html')
