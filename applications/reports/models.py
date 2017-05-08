# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class AccountingAccess(models.Model):
    user = models.OneToOneField(User)
    coming = models.DateTimeField(verbose_name='Пришел в', auto_now_add=True)
    leaving = models.DateTimeField(verbose_name='Ушел в', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user.profile.get_full_name()
