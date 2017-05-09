# -*- coding: utf-8 -*-
from django import forms

from applications.profiles.models import Profile


class Profile_form(forms.ModelForm):
        class Meta():
            model = Profile
            fields = [
            'first_name',
            'last_name',
            'position',
            'birthday',
            'image',

    ]