from django import forms
from .models import incidentReport, Resource, userProfile

class incidentReportForm(forms.ModelForm):
    class Meta:
        model = incidentReport
        fields = ['title', 'description']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'link', 'resource_type']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about yourself...',
                'rows': 4
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }