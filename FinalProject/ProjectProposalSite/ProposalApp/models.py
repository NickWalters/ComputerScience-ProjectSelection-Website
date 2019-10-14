from django.db import models
from django.contrib.auth.models import User

# this model stores the unit information, because the projects need to link to a specific unit
class UnitModel(models.Model):
    unitID = models.AutoField(primary_key=True)
    unitCode = models.CharField(max_length=32)

    def __str__(self):
        return self.unitCode

# Model for displaying and making changes to sponsor submitted projects
class ProjectModel(models.Model):
    # ID to differentiate projects
    projectID = models.AutoField(primary_key=True)
    # Admin fields providing information about the project
    approved = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    postgraduate = models.BooleanField(default=False)
    submissionDate = models.DateField(null=True, blank=True)

    # Project descriptions
    supervisor1 = models.ForeignKey(User, on_delete=models.CASCADE)
    supervisor2Title = models.CharField(max_length=20, blank=True)
    supervisor2FirstName = models.CharField(max_length=30, blank=True)
    supervisor2LastName = models.CharField(max_length=30, blank=True)
    supervisor3Title = models.CharField(max_length=20, blank=True)
    supervisor3FirstName = models.CharField(max_length=30, blank=True)
    supervisor3LastName = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    noOfStudents = models.IntegerField()
    prerequisites = models.CharField(max_length=200)
    projectTags = models.CharField(max_length=200)
    IP = models.CharField(max_length=22)
    onCampus = models.BooleanField(default=False)

    # Checkboxes for project discipline(s)
    chemical = models.BooleanField(default=False)
    civil = models.BooleanField(default=False)
    elec = models.BooleanField(default=False)
    envir = models.BooleanField(default=False)
    materials = models.BooleanField(default=False)
    mechanical = models.BooleanField(default=False)
    mechatronic = models.BooleanField(default=False)
    mining = models.BooleanField(default=False)
    oilGas = models.BooleanField(default=False)
    petroleum = models.BooleanField(default=False)
    software = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UnitProjectLink(models.Model):
    linkID = models.AutoField(primary_key=True)
    projectID = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    unitID = models.ForeignKey(UnitModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectID.title + " - " + self.unitID.unitCode

    class Meta:
        unique_together = ('projectID', 'unitID')
