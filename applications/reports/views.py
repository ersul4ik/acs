# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def report_main(request):
    template = 'main_report.html'
    return render(request, template)
