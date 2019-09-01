from django import forms

def ProjectProposalForm(forms.Form):
    title = form.CharField()
	noOfStudents = form.IntegerField()
	description = form.CharField(max_length = 90000)
	timeRequired = form.CharField(max_length = 1000)
