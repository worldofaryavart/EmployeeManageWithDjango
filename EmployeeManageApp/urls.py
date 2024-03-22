from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal/', views.personal_list, name='personal_list'),
    path('personal/add/', views.npersonal, name='npersonal'),
    path('personal/<int:pk>/modify/', views.modify_personal, name='modify_personal'),
    path('personal/<int:pk>/delete/', views.delete_personal, name='delete_personal'),
    path('personal/search/', views.search_personal, name='search_personal'),

    path('office/', views.office_list, name='office_list'),
    path('office/add/', views.noffice, name='noffice'),
    path('office/<int:pk>/modify/', views.modifyoffice, name='modifyoffice'),
    path('office/<int:pk>/delete/', views.delete_office, name='delete_office'),
    path('office/search/', views.search_office, name='search_office'),

    path('salary/', views.salary_list, name='salary_list'),
    path('salary/add/', views.nsalary, name='nsalary'),
    path('salary/<int:pk>/delete/', views.delete_salary, name='delete_salary'),
    path('salary/search/', views.search_salary, name='search_salary'),
]