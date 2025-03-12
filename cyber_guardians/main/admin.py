from django.contrib import admin
from .models import answer, userProfile, trainingModule, assessment, incidentReport, Resource, quiz, question, userProgress

admin.site.register(userProfile)
admin.site.register(trainingModule)
admin.site.register(assessment)
admin.site.register(incidentReport)
admin.site.register(Resource)
admin.site.register(quiz)
admin.site.register(question)
admin.site.register(userProgress)
admin.site.register(answer)
