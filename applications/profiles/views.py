# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from applications.profiles.models import Profile


def profile_main(request, user_id):
    template = 'profile.html'
    try:
        user = Profile.objects.get(user__id=user_id)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, template, {'user': user})
