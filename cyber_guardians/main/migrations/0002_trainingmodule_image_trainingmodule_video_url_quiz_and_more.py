# Generated by Django 5.1.7 on 2025-03-12 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodule',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload an image for the module.', null=True, upload_to='uploads/training_images/'),
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='video_url',
            field=models.URLField(blank=True, help_text='Link to a video related to the module.', null=True),
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the quiz.', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('training_module', models.ForeignKey(help_text='The training module this quiz belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='main.trainingmodule')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(help_text='The text of the question.', max_length=500)),
                ('correct_answer', models.CharField(help_text='The correct answer.', max_length=200)),
                ('answer_choices', models.JSONField(help_text='A JSON field to store multiple answer choices.')),
                ('quiz', models.ForeignKey(help_text='The quiz this question belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='quiz',
            field=models.ForeignKey(blank=True, help_text='Associated quiz for this module.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.quiz'),
        ),
        migrations.CreateModel(
            name='userProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.PositiveIntegerField(default=0, help_text='Score achieved in the associated quiz.')),
                ('training_module', models.ForeignKey(help_text='The training module completed by the user.', on_delete=django.db.models.deletion.CASCADE, to='main.trainingmodule')),
                ('user', models.ForeignKey(help_text='The user who completed the module.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
