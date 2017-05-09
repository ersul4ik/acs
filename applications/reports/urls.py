# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.reports.views import report_main

urlpatterns = [
    url(r'$', report_main, name='list'),
]
