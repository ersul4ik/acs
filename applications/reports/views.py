# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from applications.reports.models import AccountingAccess


@login_required
def report_main(request):
    template = 'main_report.html'
    access_list = AccountingAccess.objects.all()
    return render(request, template, {'user_list': access_list})
    return render(request, template, {'list': access_list})


