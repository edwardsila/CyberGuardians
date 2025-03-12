from django.contrib import admin
from .models import userProfile, trainingModule, assessment, incidentReport, Resource

admin.site.register(userProfile)
admin.site.register(trainingModule)
admin.site.register(assessment)
admin.site.register(incidentReport)
admin.site.register(Resource)