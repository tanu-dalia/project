from tokenize import Special
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.forms import CharField
# Create your models here.
class user(AbstractUser):
    pass

class user_profile(models.Model):
    user_id = models.OneToOneField(user, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="files/")
    work_experience = models.CharField(max_length=200, default='')
    qualification = models.CharField(max_length=200, default='')


class company(models.Model):
    comapany_name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    working_employes=models.CharField(max_length=200)
    Specialization=models.CharField(max_length=150)


class job_posting(models.Model):
    company_id=models.ForeignKey(company,on_delete=models.CASCADE,related_name='company_id')
    job_title=models.CharField(max_length=300)
    salary_expected=models.IntegerField()
    timing=models.IntegerField()
    type=models.CharField(max_length=200)


class job_applied(models.Model):
     student_id=models.ForeignKey(user,on_delete=models.CASCADE,related_name='student_id')
     job_id=models.ForeignKey(job_posting,on_delete=models.CASCADE,related_name='job_id')
     status=models.CharField(max_length=400)


# class notifications(models.Model):
#      user_id=models.ForeignKey(user,on_delete=models.CASCADE,related_name='user_id')
#      notification_details=models.CharField(max_length=300)
#      job_applied_id=models.ForeignKey()
#      created_at=models.CharField(max_length=200)