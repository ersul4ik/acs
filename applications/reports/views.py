# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from applications.reports.forms import SearchReportForm
from applications.reports.models import AccountingAccess


@login_required
def report_main(request, page_number=1):
    template = 'main_report.html'
    form = SearchReportForm(request.GET or None)

    if 'header_search' in request.GET:
        accounting_list = AccountingAccess.objects.filter(
            Q(user__first_name__contains=request.GET.get('username')) |
            Q(user__username__contains=request.GET.get('username'))
        )
    elif 'form_search' in request.GET:
        today = datetime.today()
        first_date = request.GET.get('first_date') or datetime.strftime(today, '%Y-%m-01')
        last_date = request.GET.get('last_date')
        last_date = today if not last_date else datetime.strptime(last_date, '%Y-%m-%d')
        last_date += timedelta(days=1)
        accounting_list = AccountingAccess.objects.filter(date__range=[first_date, last_date])
    else:
        accounting_list = AccountingAccess.objects.filter(date=datetime.today())

    if not request.user.is_superuser:
        accounting_list = accounting_list.filter(user__position__departament=request.user.get_departament())

    if request.GET.get('departament'):
        accounting_list = accounting_list.filter(user__position__departament__slug=request.GET.get('departament'))

    paginator = Paginator(accounting_list, 15)
    return render(request, template, {
        'account_list': paginator.page(page_number),
        'form': form,
    })
