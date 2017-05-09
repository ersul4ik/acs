# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.forms import CheckboxSelectMultiple

from applications.profiles.models import Profile, WorkPeriod


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1


class WorkPeriodInline(admin.StackedInline):
    model = WorkPeriod
    extra = 1


class UserAdmin(admin.ModelAdmin):
    exclude = ('first_name', 'last_name', 'user_permissions', 'password', 'is_active')
    inlines = [ProfileInline, WorkPeriodInline]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
