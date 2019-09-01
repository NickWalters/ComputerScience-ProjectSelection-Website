from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('sign_in/', views.sign_in, name='sign-in'),
    path('user_register/', views.user_register, name='user-register'),
]
