# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def page_not_found(request):
    return render(request, 'page_not_found.html')


def server_error(request):
    return render(request, 'server_error.html')
