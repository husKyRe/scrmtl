from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from . import models
# Register your models here.

from .forms import ScrumUserCreationForm, ScrumUserChangeForm, GroupAdminForm
from .models import PlatformUser


admin.site.register(models.Task)
admin.site.register(models.SteplistItem)
admin.site.register(models.Steplist)
admin.site.register(models.Project)
admin.site.register(models.Lane)
admin.site.register(models.Label)
admin.site.register(models.Feature)
admin.site.register(models.Epic)
admin.site.register(models.Board)
admin.site.register(models.File)
admin.site.register(models.ProjectUser)
admin.site.register(models.ProjectRole)
admin.site.register(models.Sprint)


class ScrumUserAdmin(UserAdmin):
    add_form = ScrumUserCreationForm
    form = ScrumUserChangeForm
    model = PlatformUser
    list_display = ('email', 'is_staff', 'is_active',
                    'is_superuser', 'username', 'name', )
    list_filter = ('email', 'is_staff', 'is_active',
                   'is_superuser', 'username', 'name', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2',
                       'is_staff', 'is_superuser', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(PlatformUser, ScrumUserAdmin)

# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.


class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
