# Generated by Django 5.1.7 on 2025-03-13 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_incidentreport_reported_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidentreport',
            name='reported_by',
        ),
    ]
