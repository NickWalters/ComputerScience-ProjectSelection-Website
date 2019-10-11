
# Project Proposal Site - Install


# environment setup
  You must have Python3 installed on your computer, and pip to install the required files
	to check your python version, you can run:
 
		 python --version

check if you have django already installed

		 python -m django --version
  
  -run commands `pip install -r requirements.txt`

		'pip install virtualenv' (Reccomended)

		'pip install django'

		'pip install django-mysql'

		'pip install django mysqlclient'


This will install all the required files and packages. 
With the mySQL database configurations made (according to your computer) we can now set up this application
	- we can now start the application with your required name/titles :
		- django-admin.py startproject mysite



  We can now input out database settings in the settings.py file, according to your SQL configuration:
	- for example:

		- USER: mysqlusername234
		- PASSWORD: notaSecret12$1


  Make sure to migrate to this new app:


		- python3 manage.py makemigrations
		- python3 manage.py migrate

# The Development server
to verify that the setup works and to run the server, put in the terminal:

	python3 manage.py runserver



	
