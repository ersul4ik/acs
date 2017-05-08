# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 06:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coming', models.DateTimeField(auto_now_add=True, verbose_name='\u041f\u0440\u0438\u0448\u0435\u043b \u0432')),
                ('leaving', models.DateTimeField(blank=True, null=True, verbose_name='\u0423\u0448\u0435\u043b \u0432')),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]