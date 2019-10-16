from django import forms
from .models import ProjectModel, UnitModel
from django.db.models import F

# Different options for Number of Students and Intellectual Property
NUMBER_OF_STUDENTS =[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
IP_OPTIONS = [("Sponsor will retain IP", "Sponsor will retain IP"), ("UWA will retain IP", "UWA will retain IP")]


# Form for project proposals including the below details to be filled by sponsors
class ProjectProposalForm(forms.Form):
    title = forms.CharField(label = 'Title of Project', max_length=100)
    description = forms.CharField(label = 'Description', widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=1000)
    supervisor2Title = forms.CharField(label='Second Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}), max_length=20)
    supervisor2FirstName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'First Name'}), max_length=30)
    supervisor2LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name'}), max_length=30)
    supervisor3Title = forms.CharField(label='Third Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}), max_length=20)
    supervisor3FirstName = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}), max_length=30)
    supervisor3LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), max_length=30)
    noOfStudents = forms.IntegerField(label = 'Number of Students Required', widget = forms.Select(choices=NUMBER_OF_STUDENTS))
    projectTags = forms.CharField(label = 'Project Tags', widget=forms.TextInput(attrs={'placeholder': 'E.g. Research, Community, Programming'}), max_length=200)
    prerequisites = forms.CharField(label = 'Prerequisites', widget=forms.TextInput(attrs={'placeholder': 'E.g. Differential Equations, Python, Linear Regression'}), max_length=200)
    onCampus = forms.BooleanField(label='Yes', required=False)
    IP = forms.CharField(label = 'IP',  widget = forms.Select(choices=IP_OPTIONS))
    chemical = forms.BooleanField(label = 'Chemical', required=False)
    civil = forms.BooleanField(label = 'Civil', required=False)
    elec = forms.BooleanField(label = 'Electrical', required=False)
    envir = forms.BooleanField(label = 'Environmental', required=False)
    materials = forms.BooleanField(label = 'Materials', required=False)
    mechanical = forms.BooleanField(label = 'Mechanical', required=False)
    mechatronic = forms.BooleanField(label = 'Mechatronic', required=False)
    mining = forms.BooleanField(label = 'Mining', required=False)
    oilGas = forms.BooleanField(label = 'Oil and Gas', required=False)
    petroleum = forms.BooleanField(label = 'Petroleum', required=False)
    software = forms.BooleanField(label = 'Software', required=False)
    other = forms.BooleanField(label = 'Other', required=False)


class EditProject(forms.ModelForm):
    title = forms.CharField(label = 'Title of Project',  max_length=50)
    description = forms.CharField(label = 'Description', widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=1000)
    supervisor2Title = forms.CharField(label='Second Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}), max_length=20)
    supervisor2FirstName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'First Name'}), max_length=30)
    supervisor2LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name'}), max_length=30)
    supervisor3Title = forms.CharField(label='Third Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}), max_length=20)
    supervisor3FirstName = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}), max_length=30)
    supervisor3LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), max_length=30)
    noOfStudents = forms.IntegerField(label = 'Number of Students Required', widget = forms.Select(choices=NUMBER_OF_STUDENTS))
    projectTags = forms.CharField(label = 'Project Tags', widget=forms.TextInput(attrs={'placeholder': 'E.g. Research, Community, Programming'}), max_length=200)
    prerequisites = forms.CharField(label = 'Prerequisites', widget=forms.TextInput(attrs={'placeholder': 'E.g. CITS2002, Python, Linear Regression'}), max_length=200)
    onCampus = forms.BooleanField(label='Yes', required=False)
    IP = forms.CharField(label = 'IP',  widget = forms.Select(choices=IP_OPTIONS))
    chemical = forms.BooleanField(label = 'Chemical', required=False)
    civil = forms.BooleanField(label = 'Civil', required=False)
    elec = forms.BooleanField(label = 'Electrical', required=False)
    envir = forms.BooleanField(label = 'Environmental', required=False)
    materials = forms.BooleanField(label = 'Materials', required=False)
    mechanical = forms.BooleanField(label = 'Mechanical', required=False)
    mechatronic = forms.BooleanField(label = 'Mechatronic', required=False)
    mining = forms.BooleanField(label = 'Mining', required=False)
    oilGas = forms.BooleanField(label = 'Oil and Gas', required=False)
    petroleum = forms.BooleanField(label = 'Petroleum', required=False)
    software = forms.BooleanField(label = 'Software', required=False)
    other = forms.BooleanField(label = 'Other', required=False)
    class Meta:
        model = ProjectModel
        fields = ['title', 'description','supervisor2Title','supervisor2FirstName','supervisor2LastName','supervisor3Title','supervisor3FirstName','supervisor3LastName',
                'noOfStudents','projectTags','prerequisites','onCampus', 'IP','chemical','civil','elec','envir','materials','mechanical','mechatronic','mining','oilGas','petroleum',
                'petroleum','software','other']
        exclude = ['supervisor1', 'draft', 'approved', 'viewable', 'postgraduate','creationDate','deadlineDate']


class UnitProjectLinkForm(forms.Form):
    projectID = forms.ModelChoiceField(label='Project', queryset=ProjectModel.objects.all().filter(approved=True).order_by(F('title').asc()))
    unitID = forms.ModelChoiceField(label='Unit', queryset=UnitModel.objects.all().order_by(F('unitCode').asc()))


class UnitForm(forms.Form):
    unitCode = forms.CharField(label='Unit Code', max_length=32)

