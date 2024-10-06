from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

def logged_out(request):
    return render(request, "registration/user_logged_out.html")
