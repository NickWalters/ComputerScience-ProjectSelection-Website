from django.urls import path
from . import views

# URLs patterns for the various parts of the website
urlpatterns = [
    path('', views.home, name='home-page'),
    path('project_list/', views.project_list, name='project-list'),
    path('project_registration/', views.project_registration, name='project-registration'),
    path('edit/<int:pk>', views.project_edit, name='project-edit'),
    path('detail/<int:pk>/', views.project_detail, name='detail'),
    path('delete/<int:pk>/', views.project_delete, name='delete'),
    path('approve/<int:pk>/', views.project_approval, name='approve'),
    path('viewable/<int:pk>/', views.project_viewable, name='viewable'),
    path('postgrad/<int:pk>/', views.project_postgrad, name='postgrad'),
    path('approveuser/<int:pk>/', views.approve_user, name='approve-user'),
    path('unit_registration', views.unit_registration, name='unit-registration')
]
