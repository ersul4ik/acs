# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.accounts import views

urlpatterns = [
    url(r'logout/$', views.logout, name='logout'),
    url(r'login/$', views.login, name='login'),
    url(r'list/$', views.user_list, name='user_list'),
    url(r'create/$', views.create_user, name='create_user'),
    url(r'(?P<username>\S+)/view/$', views.view_user, name='view_user'),
    url(r'(?P<username>\S+)/change/$', views.change_user, name='change_user'),
    url(r'(?P<username>\S+)/password/$', views.change_password, name='change_password'),
    url(r'(?P<username>\S+)/permissions/$', views.change_permissions, name='change_permissions'),
]
