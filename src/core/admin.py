#coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('User info', {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'avatar')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'avatar'),
        }),
    )

    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="self.avatar" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True
    admin_avatar.short_description = u'Аватар'


admin.site.register(User, UserAdmin)