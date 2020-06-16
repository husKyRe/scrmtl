# Generated by Django 3.0.3 on 2020-05-14 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200514_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board',
            field=models.ForeignKey(help_text='The project this board belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='api.Project'),
        ),
        migrations.AlterField(
            model_name='epic',
            name='files',
            field=models.ManyToManyField(blank=True, help_text='Files a user wants to be connected with the card', related_name='epic_files', to='api.File'),
        ),
        migrations.AlterField(
            model_name='epic',
            name='labels',
            field=models.ManyToManyField(blank=True, help_text='User defined label for the card', related_name='epic_cards', to='api.Label'),
        ),
        migrations.AlterField(
            model_name='epic',
            name='lane',
            field=models.ForeignKey(help_text='Lane this card belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='epic_cards', to='api.Lane'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='epic',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='api.Epic'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='files',
            field=models.ManyToManyField(blank=True, help_text='Files a user wants to be connected with the card', related_name='feature_files', to='api.File'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='labels',
            field=models.ManyToManyField(blank=True, help_text='User defined label for the card', related_name='feature_cards', to='api.Label'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='lane',
            field=models.ForeignKey(help_text='Lane this card belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='feature_cards', to='api.Lane'),
        ),
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.SlugField(help_text='The color of the label in hex (#ffffff)', max_length=7),
        ),
        migrations.AlterField(
            model_name='lane',
            name='board',
            field=models.ForeignKey(help_text='The board this lane is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='lanes', to='api.Board'),
        ),
        migrations.AlterField(
            model_name='task',
            name='feature',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.Feature'),
        ),
        migrations.AlterField(
            model_name='task',
            name='files',
            field=models.ManyToManyField(blank=True, help_text='Files a user wants to be connected with the card', related_name='task_files', to='api.File'),
        ),
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, help_text='User defined label for the card', related_name='task_cards', to='api.Label'),
        ),
        migrations.AlterField(
            model_name='task',
            name='lane',
            field=models.ForeignKey(help_text='Lane this card belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='task_cards', to='api.Lane'),
        ),
    ]