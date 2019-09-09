from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('project_list_undergrad/', views.project_list_undergrad, name = 'project-list-undergrad'),
    path('project_registration/', views.project_registration, name='project-registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project/<int:pk>', views.projectEdit, name='project-edit'),
]
