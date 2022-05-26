from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import user, user_profile, company, job_applied, job_posting
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='loginAdmin')
def index(request):
    return render(request, "temp/admin_layout.html")


@login_required(login_url='loginAdmin')
def home(request):
    jb = job_posting.objects.all().count()
    cp = company.objects.all().count()
    us = user_profile.objects.all().count()
    return render(request, "temp/home.html", {'jb': jb, 'cp': cp, 'us': us})

def loginAdmin(request):
    if request.method == "POST":
        # Attempt to sign user in
        name = request.POST["username"]
        password = request.POST["password"]
        print('Username - ', name, 'Password - ', password)
        result = authenticate(request, username=name, password=password)
        print('User Details - ', result)
        # Check if authentication successful
        if result is not None:
            if result.is_superuser:
                login(request, result)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "temp/login.html", {
                    "message": "Wrong User Credentials."
                })
        else:
            return render(request, "temp/login.html", {
                "message": "Invalid emailId and/or password."
            })
    else:
        return render(request, "temp/login.html")


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         qualification = request.POST['qualification']
#         work = request.POST['work']
#         resume = request.FILES['resume']
#
#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["passwords"]
#         if password != password:
#             return render(request, "temp/register.html", {
#                 "message": "Passwords must match."
#             })
#
#         # Attempt to create new user
#         try:
#             users = user.objects.create_user(username, email, password)
#             users.save()
#             user_pro = user_profile(user_id=users, resume=resume, work_experience=work, qualification=qualification)
#             user_pro.save()
#         except IntegrityError:
#             return render(request, "temp/register.html", {
#                 "message": "Username already taken."
#             })
#         return render(request, 'temp/register.html', {"message": 'Registered successfully.'})
#     else:
#         return render(request, "temp/register.html")

@login_required(login_url='loginAdmin')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginAdmin'))


@login_required(login_url='loginAdmin')
def all_companies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "temp/all_company.html", {"companies": companies})
    # return render(request, 'temp/layout.html')


@login_required(login_url='loginAdmin')
def add_company(request):
    if request.method == 'POST':
        comapany_name = request.POST['cname']
        location = request.POST['loc']
        working_employes = request.POST['number_of_employes']
        Specialization = request.POST['specilization']
        try:
            a = company(comapany_name=comapany_name, location=location, working_employes=working_employes,
                        Specialization=Specialization)
            a.save()
        except:
            return render(request, 'temp/add_company.html', {'message': 'try again'})
        return HttpResponseRedirect(reverse('all_company'))
    else:
        return render(request, 'temp/add_company.html')


@login_required(login_url='loginAdmin')
def edit_company(request, id):
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
            return render(request, 'temp/edit_company.html', {'com': com, 'message': 'try again'})
        return HttpResponseRedirect(reverse('all_company'))
    else:
        return render(request, 'temp/edit_company.html', {'com': com})


@login_required(login_url='loginAdmin')
def delete_company(request, id):
    a = company.objects.get(id=id)
    try:
        a.delete()
    except:
        return render(request, "temp/all_company.html", {'messge': 'try again'})
    return HttpResponseRedirect(reverse('all_company'))


@login_required(login_url='loginAdmin')
def all_user(request):
    stu = user_profile.objects.all()
    print(stu)
    return render(request, "temp/all_user.html", {"user": stu})
    # return render(request, 'temp/layout.html')


@login_required(login_url='loginAdmin')
def add_user(request):
    if request.method == 'POST':
        user_id = request.POST['uname']
        Email = request.POST['email']
        resume = request.FILES['resume']
        work_experience = request.POST['work_experience']
        qualification = request.POST['qualification']
        try:
            a = company(_user_id=user_id, Email=Email, resume=resume, work_experience=work_experience,
                        qualification=qualification)
            a.save()
        except:
            return render(request, 'temp/add_user.html', {'message': 'try again'})
        return HttpResponseRedirect(reverse('all_user'))
    else:
        return render(request, 'temp/add_user.html')


@login_required(login_url='loginAdmin')
def all_jobs(request):
    jp = job_posting.objects.all()
    print(jp)
    return render(request, "temp/all_jobs.html", {"jp": jp})


@login_required(login_url='loginAdmin')
def add_job(request):
    if request.method == 'POST':
        comapany_id = company.objects.get(id=request.POST['company'])
        job_title = request.POST['title']
        salary_expected = request.POST['salary']
        timing = request.POST['timings']
        type = request.POST['type']
        try:
            print('Company Id - ', comapany_id, 'Job Title - ', job_title, 'Salary - ', salary_expected, 'Timing - ',
                  timing, 'Type - ', type)
            a = job_posting(company_id=comapany_id, job_title=job_title, salary_expected=salary_expected, timing=timing,
                            type=type)
            print('Saved Data - ', a)
            a.save()
        except:
            cid = company.objects.all()
            return render(request, 'temp/add_job.html', {'message': 'try again', 'cid': cid})
        return HttpResponseRedirect(reverse('all_jobs'))
    else:
        cid = company.objects.all()
        return render(request, 'temp/add_job.html', {'cid': cid})


@login_required(login_url='loginAdmin')
def edit_job(request, id):
    if request.method == 'POST':
        comapany_id = company.objects.get(id=request.POST['company'])
        job_title = request.POST['title']
        salary_expected = request.POST['salary']
        timing = request.POST['timings']
        type = request.POST['type']
        try:
            print('Company Id - ', comapany_id, 'Job Title - ', job_title, 'Salary - ', salary_expected, 'Timing - ',
                  timing, 'Type - ', type)
            a = job_posting.objects.get(id=id)
            a.company_id = comapany_id
            a.job_title = job_title
            a.salary_expected = salary_expected
            a.timing = timing
            a.type = type
            print('Saved Data - ', a)
            a.save()
        except:
            cid = company.objects.all()
            jp = job_posting.objects.get(id=id)
            return render(request, 'temp/edit_job.html', {'message': 'try again', 'cid': cid, 'jp': jp})
        return HttpResponseRedirect(reverse('all_jobs'))
    else:
        cid = company.objects.all()
        jp = job_posting.objects.get(id=id)
        return render(request, 'temp/edit_job.html', {'cid': cid, 'jp': jp})


@login_required(login_url='loginAdmin')
def delete_job(request, id):
    a = job_posting.objects.get(id=id)
    try:
        a.delete()
    except:
        return render(request, "temp/all_jobs.html", {'messge': 'try again'})
    return HttpResponseRedirect(reverse('all_jobs'))

# @login_required(login_url='loginAdmin')
# def delete_job(request, id):
#     a = job_posting.objects.get(id=id)
#     try:
#         a.delete()
#     except:
#         return render(request, "temp/all_jobs.html", {'messge': 'try again'})
#     return HttpResponseRedirect(reverse('all_jobs'))

def usersAppliedJobs(request):
    jb = job_applied.objects.all()
    return render(request, 'temp/allAppliedJobs.html',{'jb':jb})

def changestatus(request):
    b = job_applied.objects.get(id=request.GET['id'])
    b.status = request.GET['status']
    b.save()
    return redirect(usersAppliedJobs)
