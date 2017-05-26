# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from applications.accounts.models import User


class FormProfile(forms.ModelForm):
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


class FormCreateAccount(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone',
            'home_phone',
            'gender',
            'address',
            'position',
            'photo',
            'birthday',
            'password',
            'is_staff',
            'is_active',
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'ivan92'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Иванов'}),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '709 37 99 92'}),
            'home_phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '312 67 83 98'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '5мкр 17д 1кв'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 'placeholder': 'Пароль'}),
            'is_staff': forms.CheckboxInput(),
            'is_active': forms.CheckboxInput(),
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
