from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from friendship.models import Follow


@login_required(login_url="loginUser")
def profileHome(request, slug):
    user = User.objects.get(slug=slug)
    if user in Follow.objects.following(request.user):
        exists = True
    else:
        exists = False
    context = {"user": user, "exists": exists}
    return render(request, "profile/profile.html", context)


@login_required(login_url="loginUser")
def following(request):
    friends = Follow.objects.following(request.user)
    new_users = User.objects.all().order_by("-date_joined")[:5]
    context = {"friends": friends, "newusers": new_users}
    return render(request, "home/following.html", context)


@login_required(login_url="loginUser")
def followers(request):
    friends = Follow.objects.followers(request.user)
    new_users = User.objects.all().order_by("-date_joined")[:5]
    context = {"friends": friends, "newusers": new_users}
    return render(request, "home/followers.html", context)


@login_required(login_url="loginUser")
def addFollowing(request, id):
    other_user = User.objects.get(id=id)
    Follow.objects.add_follower(request.user, other_user)
    return redirect("following")


@login_required(login_url="loginUser")
def removeFollowing(request, id):
    other_user = User.objects.get(id=id)
    Follow.objects.remove_follower(request.user, other_user)
    return redirect("following")
