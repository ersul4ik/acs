# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.profiles.views import create_profile

urlpatterns = [
    url(r'$', create_profile),
]
