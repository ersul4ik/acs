# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Departament(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название отдела')
    slug = models.SlugField(blank=True, null=True, verbose_name='Слаг')
    abbreviation = models.CharField(max_length=10, verbose_name='Аббревиатура', blank=True, null=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __unicode__(self):
        return self.title


class Position(models.Model):
    departament = models.ForeignKey(Departament, verbose_name='Отдел', related_name='positions')
    title = models.CharField(max_length=50, verbose_name='Должность')
    slug = models.SlugField(blank=True, null=True, verbose_name='Слаг')

    class Meta:
        verbose_name = '"Должность"'
        verbose_name_plural = 'Должности'

    def __unicode__(self):
        return '{} ({})'.format(self.title, self.departament.title)
