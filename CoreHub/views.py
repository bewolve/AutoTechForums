from django.shortcuts import render, redirect, HttpResponse
from userProfile.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.db.models import Q

from .forms import UserMakeForm, UpdateUserForm

# Create your views here.


# SEARCH FUNCTIONALITY AND USERS SEARCH.


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("profileHome", request.user.slug)
    else:
        form = UserMakeForm()
        if request.method == "POST":
            form = UserMakeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "There was an error registering user.")
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
    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully...")
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


@login_required(login_url="loginUser")
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect("loginUser")


def search_users(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    allUsers = User.objects.filter(
        Q(username__icontains=q)
        | Q(first_name__icontains=q)
        | Q(last_name__icontains=q)
    ).exclude(id=request.user.id)
    context = {"users": allUsers}
    return render(request, "search.html", context)
