# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from applications.reports.models import AccountingAccess


@admin.register(AccountingAccess)
class AccountingAccessAdmin(admin.ModelAdmin):
    list_display = ('date', 'full_name', 'coming', 'leaving')
