from django.db import models
from django.urls import reverse


class Project(models.Model):
    projectID = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    
    def get_absolute_url(self):
        return reverse("undergraduate_list:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.projectID
