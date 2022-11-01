from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="loginUser")
def profileHome(request, slug):
    user = User.objects.get(slug=slug)
    context = {"user": user}
    return render(request, "profile/profile.html", context)
