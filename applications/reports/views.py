# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import AccountingAccess


def report_main(request):
    template = 'main_report.html'
    access_list = AccountingAccess.objects.all()
    return render(request, template, {'list': access_list})

