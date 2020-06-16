# Generated by Django 3.0.3 on 2020-05-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200419_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='epic_files', to='api.File'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='feature_files', to='api.File'),
        ),
        migrations.AlterField(
            model_name='task',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='task_files', to='api.File'),
        ),
    ]