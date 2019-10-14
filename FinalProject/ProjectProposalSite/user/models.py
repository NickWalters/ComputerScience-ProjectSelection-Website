from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Model for a website user, contains various fields of information about them
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=120)
    Phone = models.IntegerField()
    Organisation = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
