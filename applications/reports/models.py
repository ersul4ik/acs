# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date, timedelta

from django.contrib.auth.models import User
from django.db import models


class AccountingAccess(models.Model):
    user = models.ForeignKey(User, related_name='working_time')
    coming = models.TimeField(verbose_name='Пришел в', blank=True, null=True)
    coming = models.TimeField(verbose_name='Пришел в', auto_now_add=False)
    leaving = models.TimeField(verbose_name='Ушел в', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Рабочее время'
        verbose_name_plural = 'Рабочее время'

    def __unicode__(self):
        return '{} ({})'.format(self.user.profile.get_full_name(), self.date)

    def get_working_hours(self):
        if self.coming:
            return '{} - {}'.format(self.coming, self.leaving or '')
        else:
            return 'Выходной'

    def full_name(self):
        return self.user.profile.get_full_name()

    full_name.short_description = 'Пользователь'

    @staticmethod
    def _work_time(leaving, coming):
        return datetime.combine(date.today(), leaving) - datetime.combine(date.today(), coming)

    def get_processing(self):
        if self.leaving:
            work_time = self._work_time(self.leaving, self.coming)
            if work_time >= timedelta(hours=9):
                return work_time - timedelta(hours=9)
        return '-'

    def get_defect(self):
        if self.leaving:
            work_time = self._work_time(self.leaving, self.coming)
            if work_time < timedelta(hours=9):
                return timedelta(hours=9) - work_time
        return '-'
