# coding: utf-8
from __future__ import unicode_literals

from datetime import date

from django import forms

from applications.infrastructure.models import Departament

DEPARTAMENT_CHOICES = [('', '')] + [(i.slug, i.title) for i in Departament.objects.all()]


class SearchReportForm(forms.Form):
    first_date = forms.DateField(required=False, widget=forms.TextInput(attrs={
        'class': 'datepicker form-control',
        'value': date.strftime(date.today(), '%Y-%m-%d'),
    }))
    last_date = forms.DateField(required=False, widget=forms.TextInput(attrs={
        'class': 'datepicker form-control',
        'value': date.strftime(date.today(), '%Y-%m-%d'),
    }))
    departament = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'form-control'}),
                                    choices=DEPARTAMENT_CHOICES)
