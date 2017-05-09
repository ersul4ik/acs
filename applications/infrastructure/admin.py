# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from applications.infrastructure.models import Departament
from applications.infrastructure.models import Position


class PositionInline(admin.TabularInline):
    model = Position
    prepopulated_fields = {'slug': ('title',)}
    extra = 0


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PositionInline, ]
    list_display = ('title', 'abbreviation', 'slug')
