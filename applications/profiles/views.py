# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from applications.profiles.models import Profile


def profile_edit(request, user_id):
    template = 'profile.html'
    user = get_object_or_404(Profile, user__id=user_id)
    return render(request, template, {'user': user})


def profile_list(request):
    pass
