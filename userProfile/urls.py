from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.profileHome, name="profileHome"),
    path("add/<int:id>", views.addFollowing, name="addFollowing"),
    path("remove/<int:id>", views.removeFollowing, name="removeFollowing"),
    path("<slug:slug>/following/", views.following, name="following"),
    path("<slug:slug>/followers/", views.followers, name="followers"),
]
