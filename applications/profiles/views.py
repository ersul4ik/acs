# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from applications.profiles.models import Profile


def profile_main(request):
    template = 'profile.html'
    access_list = Profile.objects.all()
    return render(request, template, {'list': access_list})

