from random import randint
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


def upload_profile_perUser(instance, filename):
    extensionOfFile = filename.split(".")[-1]
    return "profiles/@{}/display-{}.{}".format(
        instance.username, instance.first_name, extensionOfFile
    )


def upload_file_perUser(instance, filename):
    extensionOfFile = filename.split(".")[-1]
    return "profiles/@{}/CV-{}.{}".format(
        instance.username, instance.first_name, extensionOfFile
    )


GENDER_CHOICES = (("M", "Male"), ("F", "Female"))


class User(AbstractUser):
    userDisplay = models.ImageField(upload_to=upload_profile_perUser)
    userBio = models.TextField(blank=True, null=True, default="No Bio Yet...")
    userGender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    userInsta = models.TextField(blank=True, null=True)
    userFacebook = models.TextField(blank=True, null=True)
    userCV = models.FileField(null=True, blank=True, upload_to=upload_file_perUser)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = slugify("{}-{}".format(self.username, self.first_name))
        super(User, self).save(*args, **kwargs)
