# Generated by Django 3.0.3 on 2020-05-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200517_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sprint_duration',
            field=models.PositiveIntegerField(blank=True, help_text='Duration of a sprint', null=True),
        ),
    ]