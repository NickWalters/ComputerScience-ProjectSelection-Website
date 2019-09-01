from django.db import models

# 'sponsor' field, is the company that the client works for/represents
# if the client is a company, then this 'academic' variable is not nessessary
class Client(models.Model):
	userID = models.IntegerField(primary_key=True)
	firstName = models.CharField(max_length = 20)
	lastName = models.CharField(max_length = 20)
	title = models.CharField(max_length = 5)
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	mobile = models.IntegerField();
	email = models.CharField(max_length = 200)
	UWAorCompany = models.BooleanField()
	companyName = models.CharField(max_length = 50)
	companyDescription = models.CharField(max_length = 500)

# if there are more than one supervior, there information is stored here
class Supervisor(models.Model):
	supervisorID = models.IntegerField(primary_key=True)
	firstName = models.CharField(max_length = 20)
	lastName = models.CharField(max_length = 20)
	title = models.CharField(max_length = 5)

# 'supervisor' variable holds the projects main Supervisor/manager name/ID
# 'sponsor' variable contains the details of the company 'sponsoring' the project for students
# 'time required' field, is just a simple text explanation about how long the project is going to take, eg "The project takes 6 months"
class Project(models.Model):
	projectID = models.IntegerField(primary_key=True)
	supervisor = models.ForeignKey(Client, on_delete=models.CASCADE)
	#supervisor2 = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	#supervisor3 = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

	title =  models.CharField(max_length = 50)
	noOfStudents = models.IntegerField()
	description = models.CharField(max_length = 1000)
	#timeRequired = models.CharField(max_length = 100)
	confirmed = models.BooleanField(default=False)
	viewable = models.BooleanField(default=False)
	creationDate = models.DateField()
	deadlineDate = models.DateField()
    #prerequisites = models.CharField(max_length = 1000)
    #IP = models.CharField(max_length = 1000)

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

# ProjectClient is the relationship mapping projects with clients
class ProjectClient(models.Model):
	projectClientID = models.IntegerField(primary_key=True)
	clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
	projectID = models.ForeignKey(Project, on_delete=models.CASCADE)
