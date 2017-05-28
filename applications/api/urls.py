# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.api import views

urlpatterns = [
    url(r'account/$', views.account_management, name='api_commit_time'),
]
