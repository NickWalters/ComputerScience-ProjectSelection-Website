from django.db import models

# ProjectClient is the relationship mapping projects with clients
class ProjectClient(models.Model):
	projectClientID = models.IntegerField(primary_key=True)
	clientID = models.ForeignKey(Client)
	projectID = models.ForeignKey(Project)


# 'sponsor' field, is the company that the client works for/represents
# if the client is a company, then this 'academic' variable is not nessessary
class Client(models.Model):
	userID = models.IntegerField(primary_key=True)
	firstName = models.CharField()
	lastName = models.CharField()
	title = models.CharField(max_length = 20)
	username = models.CharField()
	password = models.CharField()
	mobile = models.IntegerField();
	email = models.CharField(max_length = 200)
	UWAorCompany = models.BooleanField()
	companyName = models.CharField()
	companyDescription = models.CharField()

# 'supervisor' variable holds the projects main Supervisor/manager name/ID
# 'sponsor' variable contains the details of the company 'sponsoring' the project for students
# 'time required' field, is just a simple text explanation about how long the project is going to take, eg "The project takes 6 months"
class Project(models.Model):
	projectID = models.IntegerField(primary_key=True)
	supervisor = models.ForeignKey(Client)
	supervisor2 = models.ForeignKey(Supervisor)
	supervisor3 = models.ForeignKey(Supervisor)

	title =  models.CharField()
	noOfStudents = models.IntegerField()
	description = models.CharField(max_length = 90000)
	timeRequired = models.CharField(max_length = 1000)
	confirmed = models.BooleanField(default=False)
	viewable = models.BooleanField(default=False)
	creationDate = models.DateField()
	deadlineDate = models.DateField()

	#checkboxes
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

# if there are more than one supervior, there information is stored here
class Supervisor(models.Model):
	supervisorID = models.IntegerField(primary_key=True)
	firstName = models.CharField()
	lastName = models.CharField()
	title = models.CharField(max_length = 20)
