from email import message
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . models import user, user_profile, company, job_applied, job_posting
from django.contrib.auth.decorators import login_required

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
            if user.is_superuser:
             login(request, user)
             return HttpResponseRedirect(reverse("index"))
            else:
              return render(request ,"temp/login.html",{"message":"user is not an admin"})
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
    return HttpResponseRedirect(reverse('login')) 
     
@login_required(login_url = '/login')
def all_companies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "temp/all_company.html", {"companies": companies})
    # return render(request, 'temp/layout.html')

@login_required(login_url = '/login')
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

@login_required(login_url = '/login')
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


@login_required(login_url = '/login')
def delete_company(request,id):
       a = company.objects.get(id=id)
       try:
           a.delete()
       except:
           return render(request,"temp/all_company.html", {'messge': 'try again'})
       return HttpResponseRedirect(reverse('all_company'))

@login_required(login_url = '/login')
def all_user(request):
    stu = user_profile.objects.all()
    print(stu)
    return render(request, "temp/all_user.html", {"user": stu})
    # return render(request, 'temp/layout.html')


@login_required(login_url = '/login')
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

@login_required(login_url = '/login')
def delete_user(request,id):
       a = user_profile.objects.get(id=id)
       try:
           a.delete()
       except:
           return render(request,"temp/all_user.html", {'messge': 'try again'})
       return HttpResponseRedirect(reverse('all_user'))       

@login_required(login_url = '/login')
def all_jobs(request):
    com =job_posting.objects.all()
    print(com)
    return render(request, "temp/all_jobs.html", {'company': com})
    # return render(request, 'temp/layout.html')       

@login_required(login_url = '/login')
def add_job(request):
    com = company.objects.all()
    if request.method == 'POST':
        comapany_id = request.POST['company'] 
        job_title= request.POST['title']
        salary_expected = request.POST['salary']
        time = request.POST['timing']
        type = request.POST['type']

        sel_company = company.objects.get(id=comapany_id)
        print(sel_company.id, sel_company.comapany_name, job_title, salary_expected, time, type)
        # try:
        #    a = job_posting(comapany_id = sel_company, job_title = job_title, salary_expected = salary_expected, timing = time, type= type)
        #    a.save()
        # except:
        #     return render(request,'temp/add_job.html',{'company': com , 'message':'try again'})
        # return HttpResponseRedirect(reverse('all_company'))    
        try:
            a = job_posting(company_id = sel_company, job_title = job_title, salary_expected = salary_expected, timing = time, type = type)
            a.save()
        except:
            return render(request, 'temp/add_job.html', {'company': com})
        return HttpResponseRedirect(reverse('all_jobs'))
    else:
       return render(request,'temp/add_job.html',{'company' : com})

@login_required(login_url = '/login')
def delete_job(request,id):
       a = job_posting.objects.get(id=id)
       try:
           a.delete()
       except:
           return render(request,"temp/all_jobs.html", {'messge': 'try again'})
       return HttpResponseRedirect(reverse('all_jobs'))       

@login_required(login_url = '/login')
def edit_job(request,id):
    com = job_posting.objects.get(id=id)
    comany = company.objects.all()
    if request.method == 'POST':
        company_id = request.POST['cid'] 
        job_title = request.POST['jtitle']
        salary_expected = request.POST['salary']
        timing = request.POST['timing']
        type =  request.POST['type']

        try:
           com.company_id = company_id
           com.job_title = job_title
           com.salary_expected = salary_expected
           com.timing = timing
           com.type = type
           com.save() 
        except:
            return render(request,'temp/all_jobs.html',{'com': com,'message':'try again'})
        return HttpResponseRedirect(reverse('all_job'))    
    else:
       return render(request,'temp/edit_job.html', {'com': com, 'company': comany})
       