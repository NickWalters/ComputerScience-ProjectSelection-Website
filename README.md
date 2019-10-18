# Project Proposal Site

The Project Proposal Site is a website designed for UWA staff and persons from external organisations to propose new projects for students at the university. 

## Installation

In order for the website to run, [Python](https://www.python.org/downloads/) must be installed on the computer. The package manager [pip](https://pip.pypa.io/en/stable/) is also required to install the requirements.txt file. To check to see if python and pip are installed and to see what version is installed on the computer, run: 
```
python --version
```
and
```
pip --version
```
Change the current directory to the folder .../FinalProject/ProjectProposalSite/. To run the website, a virtual environment should first be installed. If the computer is running Python 3 run the command:
```
python -m venv venv
```
Otherwise, a third party tool named [virtualenv](https://virtualenv.pypa.io/en/latest/) can be installed to create the environment. After it has been installed, run:
```
virtualenv venv
```
In order to activate the environment run one the following commands. 
For UNIX:
```
source venv/bin/activate
```
For Windows:
```
venv\Scripts\activate
```
Finally, in the directory with the `requirements.txt` file, run:
```
pip install -r requirements.txt
```
The website uses a [MySQL](https://www.mysql.com/) database which requires a server to be running. This must first be downloaded from the internet. Open MySQL and run the commands:
```
CREATE DATABSE ProjectPropsalApp;
USE DATABASE ProjectPropsalApp;
```
In the file `settings.py`, scroll down to the DATABASES and change the USER and PASSWORD fields to the same as the appropriate MySQL server:
```
'USER': 'root'
'PASSWORD': 'examplepassword'
```
  
To create all the required tables in the database, run:
```
python manage.py makemigrations
python manage.py migrate
```
  
Now, all the tables should be created in the database and the website should be ready to run.
  
## Usage
To run the website, simply type in the command:
```
python manage.py runserver
```
Once running, to view the website go to 127.0.0.1:8000