# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class AccountingAccess(models.Model):
    user = models.ForeignKey(User)
    coming = models.TimeField(verbose_name='Пришел в', blank=True, null=True)
    leaving = models.TimeField(verbose_name='Ушел в', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user.profile.get_full_name() or self.user.username

    def get_working_hours(self):
        if self.coming:
            return '{} - {}'.format(self.coming, self.leaving or '')
        else:
            return 'Выходной'
