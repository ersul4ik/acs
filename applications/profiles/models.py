# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from applications.infrastructure.models import Departament, Position


# Create your models here.
GENDER_CHOICES = (
    ('М', 'Мужской'),
    ('F', 'Женский'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    position = models.ForeignKey(Position, verbose_name='Должность')
    departament = models.ForeignKey(Departament, verbose_name='Отдел')
    leader = models.BooleanField()
    gender = models.CharField(max_length=2, verbose_name='Пол', choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    image = models.ImageField()
    age = models.IntegerField()

    def __unicode__(self):
        return self.last_name

