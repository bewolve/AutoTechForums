from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from friendship.models import Follow


@login_required(login_url="loginUser")
def profileHome(request, slug):
    user = User.objects.get(slug=slug)
    followers = Follow.objects.followers(user)
    followings = Follow.objects.following(user)
    if user in Follow.objects.following(request.user):
        exists = True
    else:
        exists = False
    context = {
        "user": user,
        "exists": exists,
        "followers": followers,
        "followings": followings,
    }
    return render(request, "profile/profile.html", context)


@login_required(login_url="loginUser")
def following(request):
    friends = Follow.objects.following(request.user)
    new_users = User.objects.all().order_by("-date_joined")[:5]
    context = {"friends": friends, "newusers": new_users}
    return render(request, "profile/following.html", context)


@login_required(login_url="loginUser")
def followers(request):
    friends = Follow.objects.followers(request.user)
    new_users = User.objects.all().order_by("-date_joined")[:5]
    context = {"friends": friends, "newusers": new_users}
    return render(request, "profile/followers.html", context)


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
