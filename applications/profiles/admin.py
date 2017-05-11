# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
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


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    # fields = ('username', 'password1', 'password2')
    # exclude = ('first_name', 'last_name', 'user_permissions', 'password', 'is_active')
    inlines = [ProfileInline, WorkPeriodInline]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
