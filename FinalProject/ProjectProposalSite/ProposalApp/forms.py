from django import forms
from .models import ProjectModel, UnitModel

# Different options for Number of Students and Intellectual Property
NUMBER_OF_STUDENTS =[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
IP_OPTIONS = [("Sponsor will retain IP", "Sponsor will retain IP"), ("UWA will retain IP", "UWA will retain IP")]


# Form for project proposals including the below details to be filled by sponsors
class ProjectProposalForm(forms.Form):
    title = forms.CharField(label = 'Title of Project')
    description = forms.CharField(label = 'Description')
    supervisor2Title = forms.CharField(label='Second Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    supervisor2FirstName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    supervisor2LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    supervisor3Title = forms.CharField(label='Third Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    supervisor3FirstName = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    supervisor3LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    noOfStudents = forms.IntegerField(label = 'Number of Students Required', widget = forms.Select(choices=NUMBER_OF_STUDENTS))
    projectTags = forms.CharField(label = 'Project Tags', widget=forms.TextInput(attrs={'placeholder': 'E.g. Research, Community, Programming'}))
    prerequisites = forms.CharField(label = 'Prerequisites', widget=forms.TextInput(attrs={'placeholder': 'E.g. CITS2002, Python, Linear Regression'}))
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
    title = forms.CharField(label = 'Title of Project')
    description = forms.CharField(label = 'Description')
    supervisor2Title = forms.CharField(label='Second Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    supervisor2FirstName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    supervisor2LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    supervisor3Title = forms.CharField(label='Third Supervisor (Optional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    supervisor3FirstName = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    supervisor3LastName = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    noOfStudents = forms.IntegerField(label = 'Number of Students Required', widget = forms.Select(choices=NUMBER_OF_STUDENTS))
    projectTags = forms.CharField(label = 'Project Tags', widget=forms.TextInput(attrs={'placeholder': 'E.g. Research, Community, Programming'}))
    prerequisites = forms.CharField(label = 'Prerequisites', widget=forms.TextInput(attrs={'placeholder': 'E.g. CITS2002, Python, Linear Regression'}))
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
                'noOfStudents','projectTags','prerequisites','IP','chemical','civil','elec','envir','materials','mechanical','mechatronic','mining','oilGas','petroleum',
                'petroleum','software','other']
        exclude = ['supervisor1', 'draft', 'approved', 'viewable', 'postgraduate','creationDate','deadlineDate']


class UnitProjectLinkForm(forms.Form):
    projectID = forms.ModelChoiceField(label='Project', queryset=ProjectModel.objects.all())
    unitID = forms.ModelChoiceField(label='Unit', queryset=UnitModel.objects.all())


class UnitForm(forms.Form):
    unitCode = forms.CharField(label='Unit Code', min_length=8, max_length=8)
    name = forms.CharField(label='Unit Name')
    description = forms.CharField(label='Description')
