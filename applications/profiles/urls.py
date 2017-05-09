# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.profiles.views import profile_main

urlpatterns = [
    url(r'(?P<user_id>\d+)/$', profile_main, name='view'),
]
