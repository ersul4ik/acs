# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_workperiod_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '\u041f\u0440\u043e\u0444\u0430\u0439\u043b', 'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0430\u0439\u043b'},
        ),
        migrations.AlterModelOptions(
            name='workperiod',
            options={'verbose_name': '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434', 'verbose_name_plural': '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434'},
        ),
    ]