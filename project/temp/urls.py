from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('login',views.log_in,name='login'),
    path('register',views.register,name='register'),
    path('logout', views.logout, name = 'logout'),
    path('all_company', views.all_companies, name="all_company"),
    path('add_company',views.add_company,name="add_company"),
    path('edit_company/<int:id>',views.edit_company,name="edit_company"),
    path('delete_company/<int:id>',views.delete_company,name="delete_company"),
    
]