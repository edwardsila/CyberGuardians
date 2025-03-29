from django.contrib import admin
from django.db import models
from .models import answer, userProfile, trainingModule, assessment, incidentReport, Resource, quiz, question, userProgress
from ckeditor.widgets import CKEditorWidget


admin.site.register(userProfile)
admin.site.register(trainingModule)
admin.site.register(assessment)
admin.site.register(incidentReport)
admin.site.register(Resource)
admin.site.register(quiz)
admin.site.register(question)
admin.site.register(userProgress)
admin.site.register(answer)

class TrainingModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'description')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
