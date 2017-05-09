# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from applications.profiles.models import Profile


class FormProfile(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('age',)
        # fields = ('first_name', 'last_name')

        # Стили полей,создание старта
        widgets = {
            'number_starts': forms.Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
