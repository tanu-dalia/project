from sqlite3 import IntegrityError
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from temp.models import user, user_profile, company, job_applied, job_posting


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        qualification = request.POST['qualification']
        work = request.POST['work']
        resume = request.FILES['resume']

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["passwords"]

        print('Username - ', username, 'Email - ', email, 'Qualification - ', qualification, 'Work Experience - ', work, 'Resume - ', resume)
        if password != password:
            return render(request, "UserSide/userRegister.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
            user_pro = user_profile(user_id=users, resume=resume, work_experience=work, qualification=qualification)
            user_pro.save()
        except IntegrityError:
            return render(request, "UserSide/userRegister.html", {
                "message": "Username already taken."
            })
        return render(request, 'UserSide/userRegister.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "UserSide/userRegister.html")


def userLogin(request):
    if request.method == "POST":
        # Attempt to sign user in
        name = request.POST["username"]
        password = request.POST["password"]
        print('Username - ', name, 'Password - ', password)
        result = authenticate(request, username=name, password=password)
        print('User Details - ', result)
        # Check if authentication successful
        if result is not None:
            if result.is_staff == 0:
                login(request, result)
                return HttpResponseRedirect(reverse("allJobs"))
            else:
                return render(request, "UserSide/userLogin.html", {
                    "message": "Wrong User Credentials."
                })
        else:
            return render(request, "UserSide/userLogin.html", {
                "message": "Invalid emailId and/or password."
            })
    else:
        return render(request, 'UserSide/userLogin.html')


def masterPage(request):
    return render(request, 'UserSide/masterPage.html')

def allJobs(request):
    jb = job_posting.objects.all()
    return render(request, 'UserSide/viewAllJobs.html',{'jb':jb})

def applyJob(request,pk):
    current_user = request.user
    current_userId = current_user.id
    print('Current User Id - ', current_userId)
    j = job_applied()
    j.student_id = request.user
    j.job_id = job_posting.objects.get(id=pk)
    j.save()
    return redirect(appliedJobs)

def appliedJobs(request):
    jb = job_applied.objects.filter(student_id_id=request.user)
    return render(request, 'UserSide/viewAllAppliedJobs.html',{'jb':jb})

def allCompanies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "UserSide/allCompanies.html", {"companies": companies})

def viewCompanyJobs(request,pk):
    print('Company Id - ', pk)
    pj = job_posting.objects.filter(company_id_id=pk)
    print(pj)
    return render(request, "UserSide/companiesJobs.html", {"pj": pj})

def logoutUser(request):
    logout(request)
    return redirect(userLogin) 



