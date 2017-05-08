from __future__ import unicode_literals

from django.contrib import admin

from applications.infrastructure.models import Departament
from applications.infrastructure.models import Position

admin.site.register(Departament)
admin.site.register(Position)
