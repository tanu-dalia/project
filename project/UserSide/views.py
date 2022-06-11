from sqlite3 import IntegrityError

from django.db.models import Q
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from temp.models import user, user_profile, company, job_applied, job_posting, ResumeModel


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

        print('Username - ', username, 'Email - ', email, 'Qualification - ', qualification, 'Work Experience - ', work,
              'Resume - ', resume)
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


@login_required(login_url='userLogin')
def masterPage(request):
    return render(request, 'UserSide/masterPage.html')


@login_required(login_url='userLogin')
def allJobs(request):
    jb = job_posting.objects.all()
    for i in jb:
        print('Job Id - ', i.id)
        ja = job_applied.objects.filter(Q(job_id_id=i.id) | Q(student_id_id=request.user))
        print('Ja Data - ', ja)
    return render(request, 'UserSide/viewAllJobs.html', {'jb': jb})


@login_required(login_url='userLogin')
def applyJob(request, pk):
    job = job_posting.objects.get(id=pk)
    already_applied = job_applied.objects.filter(student_id=request.user, job_id=job)
    print(already_applied)
    if (len(already_applied) == 0):
        # current_user = request.user
        # current_userId = current_user.id
        # print('Current User Id - ', current_userId)
        j = job_applied()
        j.student_id = request.user
        j.job_id = job
        j.save()
        return redirect(appliedJobs)
    else:
        jb = job_applied.objects.filter(student_id_id=request.user)
        return render(request, 'UserSide/viewAllAppliedJobs.html',
                      {'jb': jb, 'message': 'Already applied for the job.'})


@login_required(login_url='userLogin')
def appliedJobs(request):
    jb = job_applied.objects.filter(student_id_id=request.user)
    return render(request, 'UserSide/viewAllAppliedJobs.html', {'jb': jb})


@login_required(login_url='userLogin')
def allCompanies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "UserSide/allCompanies.html", {"companies": companies})


@login_required(login_url='userLogin')
def viewCompanyJobs(request, pk):
    print('Company Id - ', pk)
    pj = job_posting.objects.filter(company_id_id=pk)
    print(pj)
    return render(request, "UserSide/companiesJobs.html", {"pj": pj})


@login_required(login_url='userLogin')
def logoutUser(request):
    logout(request)
    return redirect(userLogin)


@login_required(login_url='userLogin')
def buildResume(request):
    if request.method == "POST":
        s = ResumeModel()
        s.profileId = request.user
        s.name = request.POST['username']
        s.email = request.POST['email']
        s.gender = request.POST["fav_language"]
        s.phonenumber = request.POST['phonenumber']
        s.github = request.POST['github']
        s.linkdin = request.POST['linkdin']
        s.skills = request.POST['skills']
        s.aboutyou = request.POST['aboutyou']
        s.tenthschool = request.POST['10']
        s.tenthpassing = request.POST['10passing']
        s.tenthpercent = request.POST['10percentage']
        s.twelveschool = request.POST['12']
        s.twelvepassing = request.POST['12passing']
        s.twelvepercent = request.POST['12percent']
        s.graduateschool = request.POST['graduation']
        s.graduatepassing = request.POST['graduationpass']
        s.graduatepercent = request.POST['graduationpercent']
        s.expereience = request.POST['experience']
        s.projects = request.POST['projects']
        s.save()
        u = user_profile.objects.get(user_id_id=request.user.id)
        return render(request, 'UserSide/buildResume.html', {"u": u})
    else:
        u = user_profile.objects.get(user_id_id=request.user.id)
        print('User Profile - ', u)
        return render(request, 'UserSide/buildResume.html', {"u": u})


def yourResume(request):
    jb = ResumeModel.objects.filter(profileId_id=request.user.id)
    return render(request, 'UserSide/yourResume.html', {"jb": jb})


def checkResume(request, pk):
    j = ResumeModel.objects.get(id=pk)
    print("Data of Resume - ", j)
    return render(request, 'UserSide/checkResume.html', {"j": j})