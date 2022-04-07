from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        # on_delete=models.CASCADE,
        on_delete=models.SET_DEFAULT,
        default="DELETEDUSER",
    )

    def __str__(self) -> str:
        return f"id {self.id} by {self.author.username} at {self.datetime_posted}"
