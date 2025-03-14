# Generated by Django 5.1.7 on 2025-03-12 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the resource.', max_length=200)),
                ('description', models.TextField(help_text='Brief description of the resource.')),
                ('link', models.URLField(help_text='URL to the resource.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource_type', models.CharField(choices=[('article', 'Article'), ('video', 'Video'), ('infographic', 'Infographic'), ('tool', 'Tool')], help_text='Type of resource.', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='trainingModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of the training module.', max_length=200)),
                ('description', models.TextField(help_text='Provide a brief description of the module.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(help_text='Main content of the training module.')),
                ('duration_minutes', models.PositiveIntegerField(help_text='Estimated duration in minutes.')),
                ('is_active', models.BooleanField(default=True, help_text='Is this module currently active?')),
            ],
        ),
        migrations.CreateModel(
            name='incidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the incident report.', max_length=200)),
                ('description', models.TextField(help_text='Detailed description of the incident.')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='open', help_text='Current status of the incident report.', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident_reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Enter the assessment question.', max_length=255)),
                ('correct_answer', models.CharField(help_text='Enter the correct answer.', max_length=255)),
                ('options', models.JSONField(help_text='Provide answer options as a JSON array.')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='main.trainingmodule')),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='Tell us about yoourself.')),
                ('profile_picture', models.ImageField(upload_to='uploads/profile/')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
