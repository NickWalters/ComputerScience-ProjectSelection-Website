from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('undergraduate_project_list/', views.project_list_undergrad, name = 'project-list-undergrad'),
    path('postgraduate_project_list/', views.project_list_postgrad, name = 'project-list-postgrad'),
    path('project_registration/', views.project_registration, name='project-registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project/<int:pk>', views.projectEdit, name='project-edit'),
    path('detail/<int:pk>/', views.project_detail, name='detail'),
]
