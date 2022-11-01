from django import forms
from userProfile.models import User
from django.contrib.auth.forms import UserCreationForm


class UserMakeForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your First Name"}),
    )  # Required
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Last Name"}),
    )

    userBio = forms.CharField(
        required=False,
        label="A short bio about yourself if you'd like",
        widget=forms.Textarea(attrs={"rows": 3}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "userBio",
            "userDisplay",
            "userGender",
            "password1",
            "password2",
        )
        labels = {
            "userDisplay": "Upload Profile Photo:",
            "userGender": "Select your gender:",
        }

        widgets = {
            "userDisplay": forms.FileInput(attrs={"accept": "image/*"}),
        }


class UpdateUserForm(forms.ModelForm):

    userBio = forms.CharField(
        required=False,
        label="A short bio about yourself if you'd like",
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    userInsta = forms.CharField(
        required=False,
        label="Your Instagram Profile Link",
        widget=forms.TextInput(),
    )
    userFacebook = forms.CharField(
        required=False,
        label="Paste your Facebook Profile Link:",
        widget=forms.TextInput(),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "userBio",
            "userInsta",
            "userFacebook",
            "userDisplay",
            "userGender",
        )
        labels = {
            "userDisplay": "Upload Profile Photo:",
            "userGender": "Select your gender:",
        }

        widgets = {
            "userDisplay": forms.FileInput(attrs={"accept": "image/*"}),
        }
