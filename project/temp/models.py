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
    comapany_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    working_employes = models.CharField(max_length=200)
    Specialization = models.CharField(max_length=150)


class job_posting(models.Model):
    company_id = models.ForeignKey(company, on_delete=models.CASCADE, related_name='company_id')
    job_title = models.CharField(max_length=300)
    salary_expected = models.IntegerField()
    timing = models.CharField(max_length=200)
    type = models.CharField(max_length=200)


class job_applied(models.Model):
    student_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name='student_id')
    job_id = models.ForeignKey(job_posting, on_delete=models.CASCADE, related_name='job_id')
    status = models.CharField(max_length=400, default='PENDING')

    def isApprove(self):
        if self.status == "APPROVED":
            return True
        else:
            return False

    def isRejected(self):
        if self.status == "REJECTED":
            return True
        else:
            return False


class ResumeModel(models.Model):
    profileId = models.OneToOneField(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    gender = models.CharField(max_length=400)
    phonenumber = models.CharField(max_length=400)
    address = models.CharField(max_length=400,default="")
    github = models.CharField(max_length=400)
    linkdin = models.CharField(max_length=400)
    skills = models.CharField(max_length=1000)
    aboutyou = models.CharField(max_length=1000)
    tenthschool = models.CharField(max_length=400)
    tenthpassing = models.CharField(max_length=400)
    tenthpercent = models.CharField(max_length=400)
    twelveschool = models.CharField(max_length=400)
    twelvepassing = models.CharField(max_length=400)
    twelvepercent = models.CharField(max_length=400)
    graduateschool = models.CharField(max_length=400)
    graduatepassing = models.CharField(max_length=400)
    graduatepercent = models.CharField(max_length=400)
    expereience = models.CharField(max_length=1000)
    projects = models.CharField(max_length=2000)
# class notifications(models.Model):
#      user_id=models.ForeignKey(user,on_delete=models.CASCADE,related_name='user_id')
#      notification_details=models.CharField(max_length=300)
#      job_applied_id=models.ForeignKey()
#      created_at=models.CharField(max_length=200)
