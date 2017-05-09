# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from applications.profiles.forms import  Profile_form
from applications.profiles.models import Profile


def profile_edit(request, user_id):
    user = get_object_or_404(Profile, user__id=user_id)
    form = Profile_form(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        form.save()
    return render(request, 'profile.html', {'form': form})


def profile_main(request, user_id):
    template = 'profile.html'
    user = Profile.objects.get(user__id=user_id)
    return render(request, template, {'user': user})

