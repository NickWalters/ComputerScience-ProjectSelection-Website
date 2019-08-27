from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Project
from .forms import UserForm

class homeView(generic.TemplateView):
    template_name = 'undergraduate_list/home.html'


class indexView(generic.ListView):
    template_name = 'undergraduate_list/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()

class detailView(generic.DetailView):
    template_name = 'undergraduate_list/detail.html'
    model = Project


class ProjectCreate(CreateView):
    model = Project
    fields = ['projectID', 'description']


class UserFormView(View):
    form_class = UserForm
    template_name = 'undergraduate_list/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form}) 

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('undergraduate_list:index')

        return render(request, self.template_name, {'form': form}) 


            