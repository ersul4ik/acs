# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime, timedelta

from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from applications.accounts.models import User
from applications.reports.models import AccountingAccess


@csrf_exempt
def account_management(request):
    """
    :request:
        finger_id, method
    Ex:
        {'finger_id': 'a1', 'method': 'enroll'}
        {'finger_id': 'a1', 'method': 'fix'}

    :response:
        0 - Успех
        1 - Нет пользователя с таким ID
        2 - Пользователь уже отметил приход (задержка час)
        3 - Не указаны параметры запроса
        4 - Не известный тип запроса
        5 - Пользователь уже отметил уход
        6 - Такой пользователь уже есть (только при enroll)
        7 - Не известный метод
    """

    if request.method != 'POST':
        return HttpResponse(4)

    method = request.POST.get('method')
    finger_id = request.POST.get('user_id')

    if method == 'fix':
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
    elif method == 'enroll':
        if not finger_id:
            return HttpResponse(3)

        user, create = User.objects.get_or_create(id_finger=finger_id, username=finger_id)

        if not create:
            return HttpResponse(1)

        user.set_password(finger_id)
        user.is_active = False
        user.save()
        return HttpResponse(0)
    else:
        return HttpResponse(7)
