from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profile(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     id = models.AutoField(primary_key=True, default=1)
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     First_Name = models.CharField(max_length=20)
#     Last_Name = models.CharField(max_length=20)
#     Email = models.EmailField(max_length=120)
#     Phone = models.IntegerField()
#     Company_Name = models.CharField(max_length=100)
#     Company_Business = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.user.username


# class Profile(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     id = models.AutoField(primary_key=True, default=1)
#     user = models.OneToOneField(User, on_delete="models.CASCADE")
#     First_Name = models.CharField(max_length=20)
#     Last_Name = models.CharField(max_length=20)
#     Email = models.EmailField(max_length=120)
#     Phone = models.IntegerField()
#     Company_Name = models.CharField(max_length=100)
#     Company_Business = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.user.username

# Model for a website user, contains various fields of information about them
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=120)
    Phone = models.IntegerField()
    Organisation_Name = models.CharField(max_length=100)
    Organisation_Business = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
