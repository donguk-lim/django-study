from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        return redirect("articles:index")
    else:
        return render(request, "accounts/signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect("articles:index")
    else:
        return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("articles:index")

def signout(request):
    if request.method == "POST":
        user = get_user(request)
        user.delete()
    return redirect("articles:index")

def myaccount(request):
    return render(request, "accounts/myaccount.html")

def update_account(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = get_user(request)
        user.email = email
        user.save()
        return redirect("accounts:myaccount")
    else:
        return render(request, "accounts/update_account.html")