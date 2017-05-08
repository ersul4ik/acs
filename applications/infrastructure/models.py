# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Departament(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название отдела')

    def __unicode__(self):
        return self.title


class Position(models.Model):
    departament = models.ForeignKey(Departament, verbose_name='Отдел')
    title = models.CharField(max_length=50, verbose_name='Должность')

    def __unicode__(self):
        return self.title
