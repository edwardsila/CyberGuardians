# Generated by Django 5.1.7 on 2025-03-29 13:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_incidentreport_reported_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmodule',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='Main content of the training module.'),
        ),
    ]
