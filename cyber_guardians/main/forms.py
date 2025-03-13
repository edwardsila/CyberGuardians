from django import forms
from .models import incidentReport, Resource

class incidentReportForm(forms.ModelForm):
    class Meta:
        model = incidentReport
        fields = ['title', 'description']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'link', 'resource_type']