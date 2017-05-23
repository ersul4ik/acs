# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from applications.reports.models import AccountingAccess


@login_required
def report_main(request):
    template = 'main_report.html'
    if 'header_search' in request.GET:
        access_list = AccountingAccess.objects.filter(user__first_name__contains=request.GET.get('username'))
    elif 'form_search' in request.GET:
        today = datetime.today()
        first_date = request.GET.get('first_date') or datetime.strftime(today, '%Y-%m-01')
        last_date = request.GET.get('last_date')
        last_date = today if not last_date else datetime.strptime(last_date, '%Y-%m-%d')
        last_date += timedelta(days=1)
        access_list = AccountingAccess.objects.filter(date__range=[first_date, last_date])
    else:
        access_list = AccountingAccess.objects.filter(date=datetime.today())
    return render(request, template, {'user_list': access_list})
