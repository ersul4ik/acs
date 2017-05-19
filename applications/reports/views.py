# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from applications.reports.models import AccountingAccess


@login_required
def report_main(request):
    template = 'main_report.html'
    if 'header_search' in request.GET:
        access_list = AccountingAccess.objects.filter(user__profile__first_name__contains=request.GET.get('username'))
    else:
        access_list = AccountingAccess.objects.filter(date=datetime.today())
    return render(request, template, {'user_list': access_list})
