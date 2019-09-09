from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=120)
    Phone = models.IntegerField()
    Company_Name = models.CharField(max_length=100)
    Company_Business = models.CharField(max_length=100)
