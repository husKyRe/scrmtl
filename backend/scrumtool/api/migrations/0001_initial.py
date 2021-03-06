# Generated by Django 3.0.3 on 2020-07-15 15:05

import api.models.model_interfaces
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import rules.contrib.models


def load_projects_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "project_initial")
#    call_command("loaddata", "board")
#    call_command("loaddata", "lane")


def delete_projects(apps, schema_editor):
    Store = apps.get_model("api", "project")
    Store.objects.all().delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                                                max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                                               max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                                            max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='This represents the name of the lane', max_length=256)),
                ('description', models.TextField(blank=True,
                                                 help_text='User description of the card', null=True)),
                ('board_type', models.CharField(choices=[('PB', 'Product Backlog Board'), ('SP', 'Sprint Backlog Board '), (
                    'AB', 'Archiv Board')], help_text='This represents the type of board', max_length=2)),
                ('display_lane_horizontal', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetProject, api.models.model_interfaces.IGetBoard),
        ),
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='User given name of the card', max_length=256)),
                ('description', models.TextField(blank=True,
                                                 help_text='User description of the card', null=True)),
                ('numbering', models.IntegerField(default=0,
                                                  help_text='Describes the order of the steps')),
                ('storypoints', models.IntegerField(default=0,
                                                    help_text='This is the name of the list itself')),
                ('status', models.CharField(choices=[('ns', 'not started'), ('do', 'done'), (
                    'ip', 'in progress')], default='ns', help_text='This is the name of the list itself', max_length=2)),
                ('assigned_users', models.ManyToManyField(blank=True, help_text='User that are assigned to the card',
                                                          related_name='epic_cards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Epic(Card)',
                'verbose_name_plural': 'Epics(Card)',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetBoard, api.models.model_interfaces.IGetProject),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='User given name of the card', max_length=256)),
                ('description', models.TextField(blank=True,
                                                 help_text='User description of the card', null=True)),
                ('numbering', models.IntegerField(default=0,
                                                  help_text='Describes the order of the steps')),
                ('storypoints', models.IntegerField(default=0,
                                                    help_text='This is the name of the list itself')),
                ('status', models.CharField(choices=[('ns', 'not started'), ('do', 'done'), (
                    'ip', 'in progress')], default='ns', help_text='This is the name of the list itself', max_length=2)),
                ('assigned_users', models.ManyToManyField(blank=True, help_text='User that are assigned to the card',
                                                          related_name='feature_cards', to=settings.AUTH_USER_MODEL)),
                ('epic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                           related_name='features', to='api.Epic')),
            ],
            options={
                'verbose_name': 'Feature(Card)',
                'verbose_name_plural': 'Features(Card)',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetBoard, api.models.model_interfaces.IGetProject),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='card_attachement')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(
                    help_text='This is the text the Label represents', max_length=256)),
                ('color', models.TextField(help_text='The color of the label in hex (#ffffff)',
                                           max_length=7, validators=[django.core.validators.RegexValidator('^#[A-Fa-f0-9]{6}$')])),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='This represents the name of the lane', max_length=256)),
                ('numbering', models.IntegerField(default=0,
                                                  help_text='Describes the order of the lanes')),
                ('board', models.ForeignKey(help_text='The board this lane is associated with',
                                            on_delete=django.db.models.deletion.CASCADE, related_name='lanes', to='api.Board')),
            ],
            options={
                'verbose_name': 'Lane',
                'verbose_name_plural': 'Lanes',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetProject, api.models.model_interfaces.IGetBoard),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='This represents the name of the lane', max_length=256)),
                ('description', models.TextField(blank=True,
                                                 help_text='User description of the card', null=True)),
                ('start', models.DateField(blank=True,
                                           help_text='Begin of the project', null=True)),
                ('end', models.DateField(blank=True,
                                         help_text='End of the project', null=True)),
                ('sprint_duration', models.PositiveIntegerField(
                    blank=True, help_text='Duration of a sprint in days', null=True)),
                ('status', models.CharField(choices=[('AR', 'Archiv'), ('AC', 'Active')],
                                            default='AC', help_text='This represents the type of board', max_length=2)),
                ('dor', models.TextField(blank=True,
                                         help_text='Definition of Ready ', null=True)),
                ('dod', models.TextField(blank=True,
                                         help_text='Definition of Done ', null=True)),
                ('numOfSprints', models.PositiveIntegerField(blank=True,
                                                             help_text='Number of Sprints possible ', null=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetProject),
        ),
        migrations.CreateModel(
            name='ProjectRole',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[
                 (1, 'product owner'), (2, 'scrum master'), (3, 'developer')], primary_key=True, serialize=False)),
            ],
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Steplist',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='defaultSteplist',
                                          help_text='This is the name of the list itself', max_length=256)),
            ],
            options={
                'verbose_name': 'Steplist',
                'verbose_name_plural': 'Steplist',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetProject, api.models.model_interfaces.IGetBoard),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    help_text='User given name of the card', max_length=256)),
                ('description', models.TextField(blank=True,
                                                 help_text='User description of the card', null=True)),
                ('numbering', models.IntegerField(default=0,
                                                  help_text='Describes the order of the steps')),
                ('storypoints', models.IntegerField(default=0,
                                                    help_text='This is the name of the list itself')),
                ('status', models.CharField(choices=[('ns', 'not started'), ('do', 'done'), (
                    'ip', 'in progress')], default='ns', help_text='This is the name of the list itself', max_length=2)),
                ('assigned_users', models.ManyToManyField(blank=True, help_text='User that are assigned to the card',
                                                          related_name='task_cards', to=settings.AUTH_USER_MODEL)),
                ('feature', models.ForeignKey(
                    blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.Feature')),
                ('files', models.ManyToManyField(
                    blank=True, help_text='Files a user wants to be connected with the card', related_name='task_files', to='api.File')),
                ('labels', models.ManyToManyField(
                    blank=True, help_text='User defined label for the card', related_name='task_cards', to='api.Label')),
                ('lane', models.ForeignKey(help_text='Lane this card belongs to',
                                           on_delete=django.db.models.deletion.CASCADE, related_name='task_cards', to='api.Lane')),
            ],
            options={
                'verbose_name': 'Task(Card)',
                'verbose_name_plural': 'Tasks(Card)',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetBoard, api.models.model_interfaces.IGetProject),
        ),
        migrations.CreateModel(
            name='SteplistItem',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(
                    help_text='This is the text the user enters', max_length=256)),
                ('checked', models.BooleanField(default=False,
                                                help_text='Indicates that the step is finished')),
                ('numbering', models.IntegerField(default=0,
                                                  help_text='Describes the order of the steps')),
                ('steplist', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.Steplist')),
            ],
            options={
                'verbose_name': 'Step',
                'verbose_name_plural': 'Step',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model,
                   api.models.model_interfaces.IGetProject, api.models.model_interfaces.IGetBoard),
        ),
        migrations.AddField(
            model_name='steplist',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='steplists', to='api.Task'),
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                              related_name='project_users', to='api.Project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                           related_name='project_users', to='api.ProjectRole')),
                ('scrum_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                                 related_name='project_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ProjectUser',
                'verbose_name_plural': 'ProjectUsers',
            },
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='feature',
            name='files',
            field=models.ManyToManyField(
                blank=True, help_text='Files a user wants to be connected with the card', related_name='feature_files', to='api.File'),
        ),
        migrations.AddField(
            model_name='feature',
            name='labels',
            field=models.ManyToManyField(
                blank=True, help_text='User defined label for the card', related_name='feature_cards', to='api.Label'),
        ),
        migrations.AddField(
            model_name='feature',
            name='lane',
            field=models.ForeignKey(help_text='Lane this card belongs to',
                                    on_delete=django.db.models.deletion.CASCADE, related_name='feature_cards', to='api.Lane'),
        ),
        migrations.AddField(
            model_name='epic',
            name='files',
            field=models.ManyToManyField(
                blank=True, help_text='Files a user wants to be connected with the card', related_name='epic_files', to='api.File'),
        ),
        migrations.AddField(
            model_name='epic',
            name='labels',
            field=models.ManyToManyField(
                blank=True, help_text='User defined label for the card', related_name='epic_cards', to='api.Label'),
        ),
        migrations.AddField(
            model_name='epic',
            name='lane',
            field=models.ForeignKey(help_text='Lane this card belongs to',
                                    on_delete=django.db.models.deletion.CASCADE, related_name='epic_cards', to='api.Lane'),
        ),
        migrations.AddField(
            model_name='board',
            name='project',
            field=models.ForeignKey(help_text='The project this board belongs to',
                                    on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='api.Project'),
        ),
        # migrations.RunPython(
        #    code=load_projects_from_fixture,
        #    reverse_code=delete_projects,
        # ),
    ]
