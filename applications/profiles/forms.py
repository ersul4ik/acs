# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from applications.profiles.models import Profile


class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            # 'first_name',
            'position',
            'birthday',
        )
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
        }


class FormLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Имя пользователя',
            'class': 'form-control'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }
    ))
