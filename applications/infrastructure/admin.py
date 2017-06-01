# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
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


default_site = 'Администрирование сайта'
admin.site.site_header = getattr(settings, 'SITE_HEADER', default_site)
admin.site.site_title = getattr(settings, 'SITE_TITLE', default_site)
