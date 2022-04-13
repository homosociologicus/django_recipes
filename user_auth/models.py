from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default="default_profile_picture.jpg",
        upload_to="profile_pictures",
    )

    def __str__(self) -> str:
        return f"{self.user.username} profile"
