from django.shortcuts import render, redirect
from friendship.models import Follow
from django.contrib.auth.decorators import login_required
from userProfile.models import User

# Create your views her
def home(request):
    if request.user.is_authenticated:
        # return redirect("feed")
        pass
    else:
        return redirect("registerUser")
