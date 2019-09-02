from django import forms

NUMBER_OF_STUDENTS =[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
IP_OPTIONS = [("Sponsor will retain IP", "Sponsor will retain IP"), ("UWA will retain IP", "UWA will retain IP")]

class ProjectProposalForm(forms.Form):
    title = forms.CharField(label = 'Title')
    description = forms.CharField(label = 'Description')
    noOfStudents = forms.IntegerField(label = 'Number of students', widget = forms.Select(choices=NUMBER_OF_STUDENTS))
    projectTags = forms.CharField(label = 'Project Tags')
    prerequisites = forms.CharField(label = 'Prerequisites')
    IP = forms.CharField(label = 'IP',  widget = forms.Select(choices=IP_OPTIONS))
    chemical = forms.BooleanField(label = 'Chemical')
    civil = forms.BooleanField(label = 'Civil')
    elec = forms.BooleanField(label = 'Electrical')
    envir = forms.BooleanField(label = 'Environmental')
    materials = forms.BooleanField(label = 'Materials')
    mechanical = forms.BooleanField(label = 'Mechanical')
    mechatronic = forms.BooleanField(label = 'Mechatronic')
    mining = forms.BooleanField(label = 'Mining')
    oilGas = forms.BooleanField(label = 'Oil and Gas')
    petroleum = forms.BooleanField(label = 'Petroleum')
    software = forms.BooleanField(label = 'Software')
    other = forms.BooleanField(label = 'Other')

class userRegistrationForm(forms.Form):
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=120)
    phone = forms.IntegerField()
    companyName = forms.CharField(max_length=100)
    companyBusiness = forms.CharField(max_length=100)
