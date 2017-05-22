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
    position = models.ForeignKey(Position, verbose_name='Должность', null=True)
    gender = models.CharField(max_length=2, verbose_name='Пол', choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    home_phone = models.CharField(max_length=15, verbose_name='Домашний телефон', blank=True, null=True)
    address = models.CharField(max_length=50, verbose_name='Адрес')
    photo = models.ImageField(blank=True, null=True, verbose_name='Фотография', upload_to='media/photo')
    birthday = models.DateField(verbose_name='Дата рождения', null=True)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

    def __unicode__(self):
        return self.get_full_name()

    def get_departament(self):
        return self.position.departament.title if self.position else ''

    def get_departament_abbreviation(self):
        return self.position.departament.abbreviation if self.position else ''

    def get_position(self):
        return self.position.title if self.position else ''

    def get_name_and_departament(self):
        d = ''
        if self.get_departament_abbreviation():
            d = ' ({})'.format(self.get_departament_abbreviation())
        return '{}{}'.format(self.get_full_name() or self.username, d)


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


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.get_or_create(user=instance)
