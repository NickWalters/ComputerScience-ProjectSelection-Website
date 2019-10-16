from django.urls import path
from . import views

# Patterns for the site's URLs
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/update_profile', views.update_profile, name='update-profile'),
    path('profile/<int:pk>/password_change', views.password_change, name='password_change'),
    path('users/', views.user_list, name='user-list'),
    path('approveuser/<int:pk>/', views.approve_user, name='approve-user'),
    path('deleteuser/<int:pk>/', views.delete_user, name='delete-user'),
]
