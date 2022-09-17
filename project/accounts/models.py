from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    avatar = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.user.username