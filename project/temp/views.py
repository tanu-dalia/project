from email import message
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . models import user, user_profile, company, job_applied, job_posting

# Create your views here.
def index(request):
    return render(request,"temp/admin_layout.html")

def log_in(request):
    if request.method == "POST":
        # Attempt to sign user in
        name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=name,
        password=password, is_superuser = 1)
        print(user)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "temp/login.html", {
            "message": "Invalid emailId and/or password."
        })
    else:
        return render(request, "temp/login.html")



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        qualification = request.POST['qualification']
        work = request.POST['work']
        resume = request.FILES['resume']

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["passwords"]
        if password != password:
            return render(request, "temp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
            user_pro = user_profile(user_id = users, resume = resume, work_experience = work, qualification = qualification)
            user_pro.save()
        except IntegrityError:
            return render(request, "temp/register.html", {
                "message": "Username already taken."
            })
        return render(request, 'temp/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "temp/registers.html") 


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))      
     

def all_companies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "temp/all_company.html", {"companies": companies})
    # return render(request, 'temp/layout.html')


def add_company(request):
    if request.method == 'POST':
        comapany_name = request.POST['cname'] 
        location = request.POST['loc']
        working_employes = request.POST['number_of_employes']
        Specialization = request.POST['specilization']
        try:
           a = company(comapany_name = comapany_name,location=location,working_employes=working_employes,Specialization=Specialization)
           a.save()
        except:
            return render(request,'temp/add_company.html',{'message':'try again'})
        return HttpResponseRedirect(reverse('all_company'))    
    else:
       return render(request,'temp/add_company.html')

def edit_company(request,id):
    com = company.objects.get(id=id)
    if request.method == 'POST':
        comapany_name = request.POST['cname'] 
        location = request.POST['loc']
        working_employes = request.POST['number_of_employes']
        Specialization = request.POST['specilization']
        try:
           com.comapany_name = comapany_name
           com.location = location
           com.working_employes = working_employes
           com.Specialization = Specialization
           com.save()
        except:
            return render(request,'temp/edit_company.html',{'com': com,'message':'try again'})
        return HttpResponseRedirect(reverse('all_company'))    
    else:
       return render(request,'temp/edit_company.html', {'com': com})


def delete_company(request,id):
       a = company.objects.get(id=id)
       try:
           a.delete()
       except:
           return render(request,"temp/all_company.html", {'messge': 'try again'})
       return HttpResponseRedirect(reverse('all_company'))


def all_user(request):
    stu = user_profile.objects.all()
    print(stu)
    return render(request, "temp/all_user.html", {"user": stu})
    # return render(request, 'temp/layout.html')

def add_user(request):
    if request.method == 'POST':
        user_id = request.POST['uname'] 
        Email = request.POST['email']
        resume= request.FILES['resume']
        work_experience = request.POST['work_experience']
        qualification= request.POST['qualification']
        try:
           a = company(_user_id = user_id,Email=Email,resume=resume,work_experience=work_experience,qualification=qualification)
           a.save()
        except:
            return render(request,'temp/add_user.html',{'message':'try again'})
        return HttpResponseRedirect(reverse('all_user'))    
    else:
       return render(request,'temp/add_user.html')    

def all_jobs(request):
    com = company.objects.all()
    print(com)
    return render(request, "temp/all_company.html", {"company": com})
    # return render(request, 'temp/layout.html')       

def add_job(request):
    if request.method == 'POST':
        comapany_id = request.POST['company'] 
        job_title= request.POST['title']
        salary_expected = request.POST['salary']
        timing = request.POST['timimg']
        type = request.POST['type']
        try:
           a = company(comapany_id = comapany_id,job_title=job_title,salary_expected=salary_expected,timing=timing, type= type)
           a.save()
        except:
            return render(request,'temp/add_job.html',{'message':'try again'})
        return HttpResponseRedirect(reverse('all_company'))    
    else:
       return render(request,'temp/add_job.html')