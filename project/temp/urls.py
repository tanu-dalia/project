from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('home',views.home,name='home'),
    path('loginAdmin',views.loginAdmin,name='loginAdmin'),
    path('logoutAdmin', views.logout_view, name = 'logoutAdmin'),
    path('all_company', views.all_companies, name="all_company"),
    path('add_company',views.add_company,name="add_company"),
    path('edit_company/<int:id>',views.edit_company,name="edit_company"),
    path('delete_company/<int:id>',views.delete_company,name="delete_company"),
    path('all_user',views.all_user,name="all_user"),
    path('add_user',views.add_user,name="add_user"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('add_job',views.add_job,name="add_job"),
    path('all_jobs',views.all_jobs,name="all_jobs"),
    path('edit_job/<int:id>',views.edit_job,name="edit_job"),
    path('delete_job/<int:id>',views.delete_job,name="delete_job"),
    path('usersAppliedJobs',views.usersAppliedJobs,name="usersAppliedJobs"),
    path("changestatus/",views.changestatus,name="changestatus"),
]

