from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('sign_in/', views.sign_in, name='sign-in'),
    path('project_registration/', views.project_registration, name='project-registration'),
    path('user_registration/', views.user_registration, name='user-registration'),
]
