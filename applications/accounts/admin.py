# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from applications.accounts.forms import CustomUserChangeForm
from applications.accounts.models import User, WorkPeriod


class WorkPeriodInline(admin.StackedInline):
    model = WorkPeriod
    extra = 0


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    form = CustomUserChangeForm
    inlines = [WorkPeriodInline, ]
    list_display = ('username', 'get_full_name', 'gender',
                    'id_finger', 'get_position_title',
                    'get_departament_title', 'phone', 'is_active')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'id_finger'),
        }),
        ('Перснальная информация', {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'birthday',
                'photo', 'gender', 'position',
            ),
        }),
        ('Контакты', {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'home_phone', 'address'),
        }),
        ('Безопасность (права доступа)', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions')
        }),
    )

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'id_finger'),
        }),
        ('Перснальная информация', {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'birthday',
                'photo', 'gender', 'position',
            ),
        }),
        ('Контакты', {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'home_phone', 'address'),
        }),
        ('Безопасность (права доступа)', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions',
                       'last_login', 'date_joined'),
        }),
    )
