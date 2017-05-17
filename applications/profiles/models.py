# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from applications.infrastructure.models import Departament, Position

GENDER_CHOICES = (
    ('М', 'Мужской'),
    ('F', 'Женский'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    position = models.ForeignKey(Position, verbose_name='Должность', null=True)
    gender = models.CharField(max_length=2, verbose_name='Пол', choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    home_phone = models.CharField(max_length=15, verbose_name='Домашний телефон', blank=True, null=True)
    address = models.CharField(max_length=50, verbose_name='Адрес')
    image = models.ImageField(blank=True, null=True, verbose_name='Фотография')
    birthday = models.DateField(verbose_name='Дата рождения', null=True)
    active = models.BooleanField(verbose_name='Активен', default=False)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайл'

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_departament(self):
        return self.position.departament.title

    def get_departament_abbreviation(self):
        return self.position.departament.abbreviation or ''

    def get_position(self):
        return self.position.title

    def get_name_and_departament(self):
        d = ''
        if self.get_departament_abbreviation():
            d = ' ({})'.format(self.get_departament_abbreviation())
        return '{}{}'.format(self.get_full_name(), d)


class WorkPeriod(models.Model):
    user = models.OneToOneField(User)
    employed = models.DateField(verbose_name='Принят на работу с ', blank=True, null=True)
    dismissed = models.DateField(verbose_name='Уволен с ', blank=True, null=True)
    reason_for_leaving = models.TextField(blank=True, null=True, verbose_name='Причина увольнения')

    class Meta:
        verbose_name = 'Рабочий период'
        verbose_name_plural = 'Рабочий период'

    def __unicode__(self):
        return self.user.profile.get_full_name() or self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
