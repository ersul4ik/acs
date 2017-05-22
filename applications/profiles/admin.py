# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _

from applications.profiles.models import Profile, WorkPeriod


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1


class WorkPeriodInline(admin.StackedInline):
    model = WorkPeriod
    extra = 0


class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    inlines = [ProfileInline, WorkPeriodInline]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
