# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 06:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employed', models.DateField(blank=True, null=True, verbose_name='\u041f\u0440\u0438\u043d\u044f\u0442 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 ')),
                ('dismissed', models.DateField(blank=True, null=True, verbose_name='\u0423\u0432\u043e\u043b\u0435\u043d \u0441 ')),
                ('reason_for_leaving', models.TextField(blank=True, null=True, verbose_name='\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='departament',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='leader',
        ),
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False, verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2017, 5, 8, 6, 29, 57, 986374, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='home_phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('\u041c', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), ('F', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')], max_length=2, verbose_name='\u041f\u043e\u043b'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]