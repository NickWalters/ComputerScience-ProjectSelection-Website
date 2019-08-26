from django.db import models

class Project(models.Model):
    projectID = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.projectID