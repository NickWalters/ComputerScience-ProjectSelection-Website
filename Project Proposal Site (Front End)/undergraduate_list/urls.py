"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from undergraduate_list import views

app_name = 'undergraduate_list'

urlpatterns = [
    #/undergraduate_list/
    path("", views.indexView.as_view(), name='index'),

    #undergraduate_list/register
    path("register/", views.UserFormView.as_view(), name='regiser'),

    #/undergraduate_list/1/
    re_path(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),

    #undergraduate_list/add
    re_path(r'add/$', views.ProjectCreate.as_view(), name='project-add'),

]
