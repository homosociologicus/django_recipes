# from distutils.command.upload import upload
# from email.policy import default
# from pyexpat import model
# from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default="default_profile_picture.jpg",
        upload_to="profile_pictures",
    )

    def __str__(self) -> str:
        return f"{self.user.username} profile"

    # should be updated to be compatible with AWS' S3
    # def save(self, *args, **kwargs) -> None:
    #     super().save(*args, **kwargs)

    #     # getting the square
    #     img = Image.open(self.profile_picture.path)
    #     w, h = img.size
    #     target_w, target_h = 320, 320
    #     if w > target_w or h > target_h:
    #         min_dim = min(img.size)
    #         left = (w - min_dim) / 2
    #         top = (h - min_dim) / 2
    #         right = (w + min_dim) / 2
    #         bottom = (h + min_dim) / 2
    #         img = img.crop((left, top, right, bottom))
    #         img.thumbnail((target_w, target_h))
    #         img.save(self.profile_picture.path)
