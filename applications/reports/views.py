# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta, date

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from applications.accounts.models import User
from applications.reports.models import AccountingAccess


@login_required
def report_main(request, page_number=1):
    template = 'main_report.html'
    if 'header_search' in request.GET:
        accounting_list = AccountingAccess.objects.filter(user__first_name__contains=request.GET.get('username'))
    elif 'form_search' in request.GET:
        today = datetime.today()
        first_date = request.GET.get('first_date') or datetime.strftime(today, '%Y-%m-01')
        last_date = request.GET.get('last_date')
        last_date = today if not last_date else datetime.strptime(last_date, '%Y-%m-%d')
        last_date += timedelta(days=1)
        accounting_list = AccountingAccess.objects.filter(date__range=[first_date, last_date])
    else:
        accounting_list = AccountingAccess.objects.filter(date=datetime.today())
    paginator = Paginator(accounting_list, 5)
    return render(request, template, {'user_list': paginator.page(page_number)})


@csrf_exempt
def api_commit_time(request):
    """
    :request:
        user_id

    :response:
        0 - Успех
        1 - Нет пользователя с таким ID
        2 - Пользователь уже отметил приход (задержка час)
        3 - Не указаны параметры запроса
        4 - Не верный тип запроса
        5 - Пользователь уже отметил уход
    """

    if request.method != 'POST':
        return HttpResponse(4)
    finger_id = request.POST.get('user_id')

    if not finger_id:
        return HttpResponse(3)

    try:
        user = User.objects.get(id_finger=finger_id)
    except User.DoesNotExist:
        return HttpResponse(1)

    access, create = AccountingAccess.objects.get_or_create(user=user, date=datetime.today())

    if not create:
        delay = datetime.combine(date.today(), access.coming) + timedelta(hours=1)
        if datetime.now() < delay:
            return HttpResponse(2)
        elif not access.leaving:
            access.leaving = timezone.now()
            access.save()
            return HttpResponse(0)
        else:
            return HttpResponse(5)

    access.coming = timezone.now()
    access.save()
    return HttpResponse(0)
