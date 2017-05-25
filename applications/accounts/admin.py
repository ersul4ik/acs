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
    list_display = ('username', 'get_full_name', 'gender',
                    'id_finger', 'get_position',
                    'get_departament', 'phone')
    inlines = [WorkPeriodInline, ]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
