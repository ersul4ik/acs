# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from applications.profiles.forms import FormProfile
from applications.profiles.models import Profile


def profile_edit(request, user_id):
    profile = get_object_or_404(Profile, user__id=user_id)
    form = FormProfile(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        form.save()
    return render(request, 'profile.html', {
        'form': form,
        'profile': profile,
    })


def profile_main(request, user_id):
    template = 'profile.html'
    user = Profile.objects.get(user__id=user_id)
    return render(request, template, {'user': user})


def user_login(request):
    template = 'login.html'
    return render(request, template)
