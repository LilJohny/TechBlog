from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from account.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, "account/dashboard.html")


def register(request):
    if request.method == "GET":

        return render(request, "account/register.html", {"form": CustomUserCreationForm})

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            user = form.save()
            login(request, user)

            return redirect(reverse("dashboard"))
