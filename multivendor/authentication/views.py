from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, "signin.html")

def main(request):
    return render(request, "main.html")

def home1(request):
    return render(request, "index.html")
# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email  = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        # pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "your account has been successfully created")
        return redirect('signin')

    return render(request, "signup.html")

def signin(request):
    n = ''
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username, password = pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('/main')
        
        else:
            n = 'incorrect credenials'
            

       
    return render(request, "signin.html", {'n':n})

def signout(request):
    return render(request, "signout.html")  