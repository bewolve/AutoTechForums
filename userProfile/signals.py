from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
from .models import User
import os


@receiver(post_delete, sender=User)
def delete_pfp_on_User_delete(sender, instance, **kwargs):
    if os.path.isfile(instance.userDisplay.path):
        print(instance.image.path)
