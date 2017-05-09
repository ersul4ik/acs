# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin


default_site = 'Администрирование сайта'
admin.site.site_header = getattr(settings, 'SITE_HEADER', default_site)
admin.site.site_title = getattr(settings, 'SITE_TITLE', default_site)
