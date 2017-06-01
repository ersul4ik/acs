# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta, date

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from applications.accounts.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone',
            'home_phone',
            'gender',
            'address',
            'position',
            'photo',
            'birthday',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'home_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        birthday = cleaned_data.get('birthday')
        minimum_age = date.today() - timedelta(weeks=4*12*18)

        if minimum_age < birthday:
            msg = 'Возраст пользователя не может быть младше 18 лет (%s)' % minimum_age
            self.add_error('birthday', msg)


class LoginForm(AuthenticationForm):
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


class CustomUserChangeForm(UserChangeForm):
    def clean(self):
        cleaned_data = super(CustomUserChangeForm, self).clean()
        birthday = cleaned_data.get('birthday')
        minimum_age = date.today() - timedelta(weeks=4*12*18)

        if minimum_age < birthday:
            msg = 'Возраст пользователя не может быть младше 18 лет (%s)' % minimum_age
            self.add_error('birthday', msg)
