from django.shortcuts import render, redirect, HttpResponse
from userProfile.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate


from .forms import UserMakeForm, UpdateUserForm

# Create your views here.


# REDIRECT TO PROFILE AFTER COMPELETION NEEDED!!!


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("profileHome", request.user.slug)
    else:
        form = UserMakeForm()
        if request.method == "POST":
            form = UserMakeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profileHome", request.user.slug)

        context = {"form": form}
        return render(request, "authentication/register.html", context)


@login_required(login_url="loginUser")
def updateUser(request):
    user = request.user
    form = UpdateUserForm(instance=user)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profileHome", request.user.slug)
    context = {"form": form}
    return render(request, "authentication/update.html", context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("profileHome", request.user.slug)
    else:
        form = AuthenticationForm()
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("profileHome", request.user.slug)

        context = {"form": form}
        return render(request, "authentication/login.html", context)


@login_required(login_url="loginUser")
def logoutUser(request):
    logout(request)
    return redirect("loginUser")
