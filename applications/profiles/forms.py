# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from applications.profiles.models import Profile


class FormProfile(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Имя',
            'class': 'form-control'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Фамилия',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'position',
            'birthday',
            'image',
        ]
