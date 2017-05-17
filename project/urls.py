# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from applications.reports.views import report_main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('applications.profiles.urls', namespace='profiles')),
    # url(r'^reports/', include('applications.reports.urls', namespace='reports')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'applications.administration.views.page_not_found'
handler500 = 'applications.administration.views.server_error'

urlpatterns += (
    url(r'^$', report_main, name='home_page'),
)
