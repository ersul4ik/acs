# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.accounts import views

urlpatterns = [
    url(r'logout/$', views.logout, name='logout'),
    url(r'login/$', views.login, name='login'),
    url(r'list/$', views.user_list, name='user_list'),
    url(r'(?P<username>\S+)/$', views.change_user, name='change_user'),
]
