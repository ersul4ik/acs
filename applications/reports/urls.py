# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.reports.views import report_main, api_commit_time

urlpatterns = [
    url(r'api/commit/$', api_commit_time, name='api_commit_time'),
    url(r'(\d+)/$', report_main, name='reports_page'),
]
