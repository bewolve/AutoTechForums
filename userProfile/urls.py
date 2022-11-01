from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.profileHome, name="profileHome"),
    path("add/<int:id>", views.addFollowing, name="addFollowing"),
    path("remove/<int:id>", views.removeFollowing, name="removeFollowing"),
    path("following/", views.following, name="following"),
    path("followers/", views.followers, name="followers"),
]
