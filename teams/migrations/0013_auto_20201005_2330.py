# Generated by Django 2.2.5 on 2020-10-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
