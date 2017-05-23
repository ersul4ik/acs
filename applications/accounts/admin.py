# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from applications.accounts.models import User, WorkPeriod


class WorkPeriodInline(admin.StackedInline):
    model = WorkPeriod
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [WorkPeriodInline, ]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
