from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return render(request, 'users/accounts/dashboard.html')
        else:
            context = {"error": "password or username is incorrect"}
            return render(request, "users/accounts/login.html", context)
    return render(request, "users/accounts/login.html", {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'users/accounts/login.html')