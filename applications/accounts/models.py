# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from applications.infrastructure.models import Position

GENDER_CHOICES = (
    ('М', 'Мужской'),
    ('F', 'Женский'),
)


class User(AbstractUser):
    position = models.ForeignKey(verbose_name='Должность', to=Position, null=True)
    gender = models.CharField(verbose_name='Пол', max_length=2, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=15, null=True)
    home_phone = models.CharField(verbose_name='Домашний телефон', max_length=15, blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=50, null=True)
    photo = models.ImageField(verbose_name='Фотография', upload_to='media/photo', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True)
    id_finger = models.CharField(verbose_name='ID пальца', max_length=20, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __unicode__(self):
        return self.get_full_name() or self.username

    def get_full_name(self):
        return super(User, self).get_full_name()

    get_full_name.short_description = 'Полное имя пользователя'

    def get_departament(self):
        return self.position.departament.title if self.position else ''

    def get_departament_abbreviation(self):
        return self.position.departament.abbreviation if self.position else ''

    def get_position(self):
        return self.position.title if self.position else ''

    get_position.short_description = 'Должность'

    def get_name_and_departament(self):
        d = ''
        if self.get_departament_abbreviation():
            d = ' ({})'.format(self.get_departament_abbreviation())
        return '{}{}'.format(self.get_full_name() or self.username, d)

    get_departament.short_description = 'Отдел'


class WorkPeriod(models.Model):
    user = models.ForeignKey(User)
    employed = models.DateField(verbose_name='Принят на работу с ', blank=True, null=True)
    dismissed = models.DateField(verbose_name='Уволен с ', blank=True, null=True)
    reason_for_leaving = models.TextField(blank=True, null=True, verbose_name='Причина увольнения')

    class Meta:
        verbose_name = 'Рабочий период'
        verbose_name_plural = 'Рабочий период'

    def __unicode__(self):
        return '{} | dismissed: {}'.format(self.username, self.dismissed)
