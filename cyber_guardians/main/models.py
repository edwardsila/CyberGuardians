from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class userProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True, help_text="Tell us about yoourself.")
	profile_picture = models.ImageField(upload_to='uploads/profile/')
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.user.username}'s Profile"


class trainingModule(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the training module.")
    description = models.TextField(help_text="Provide a brief description of the module.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(help_text="Main content of the training module.")
    duration_minutes = models.PositiveIntegerField(help_text="Estimated duration in minutes.")
    is_active = models.BooleanField(default=True, help_text="Is this module currently active?")

    def __str__(self):
    	return self.title



class assessment(models.Model):
    module = models.ForeignKey(trainingModule, on_delete=models.CASCADE, related_name='assessments')
    question = models.CharField(max_length=255, help_text="Enter the assessment question.")
    correct_answer = models.CharField(max_length=255, help_text="Enter the correct answer.")
    options = models.JSONField(help_text="Provide answer options as a JSON array.")

    def __str__(self):
        return f"Assessment for {self.module.title}: {self.question}"



class incidentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incident_reports')
    title = models.CharField(max_length=200, help_text="Title of the incident report.")
    description = models.TextField(help_text="Detailed description of the incident.")
    reported_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], default='open', help_text="Current status of the incident report.")

    def __str__(self):
        return f"Incident Report: {self.title} by {self.user.username}"



class Resource(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the resource.")
    description = models.TextField(help_text="Brief description of the resource.")
    link = models.URLField(help_text="URL to the resource.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resource_type = models.CharField(max_length=50, choices=[
        ('article', 'Article'),
        ('video', 'Video'),
        ('infographic', 'Infographic'),
        ('tool', 'Tool'),
    ], help_text="Type of resource.")

    def __str__(self):
        return self.title


