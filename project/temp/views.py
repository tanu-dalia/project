from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

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
    
     