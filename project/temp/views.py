from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . models import user, user_profile

# Create your views here.
def index(request):
    return render(request,"temp/layout.html")

def log_in(request):
    if request.method == "POST":
        # Attempt to sign user in
        Email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, Email=Email,
        password=password)
        # Check if authentication successful
        if user is not None:
            log_in(request, user)
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


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))      
     