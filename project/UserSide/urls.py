from django.urls import path
from . import views

urlpatterns = [
    path('userLogin', views.userLogin, name='userLogin'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('masterPage', views.masterPage, name='masterPage'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('allJobs', views.allJobs, name='allJobs'),
    path('applyJob/<int:pk>', views.applyJob, name='applyJob'),
    path('appliedJobs', views.appliedJobs, name='appliedJobs'),
    path('allCompanies', views.allCompanies, name='allCompanies'),
    path('viewCompanyJobs/<int:pk>', views.viewCompanyJobs, name='viewCompanyJobs'),
    path('buildResume', views.buildResume, name='buildResume'),
    path('checkResume/<int:pk>', views.checkResume, name='checkResume'),
    path('yourResume',views.yourResume,name="yourResume")
]
