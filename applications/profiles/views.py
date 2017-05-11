# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from applications.profiles.forms import FormProfile, FormLogin
from applications.profiles.models import Profile


@login_required
def profile_edit(request, user_id):
    profile = get_object_or_404(Profile, user__id=user_id)
    form = FormProfile(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        form.save()
    return render(request, 'profile.html', {
        'form': form,
        'profile': profile,
    })


@login_required
def profile_main(request, user_id):
    template = 'profile.html'
    user = Profile.objects.get(user__id=user_id)
    return render(request, template, {'user': user})


def user_login(request):
    template = 'login.html'
    form = FormLogin(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect(request.GET.get('next') or '/')
    return render(request, template, {'form': form})


def user_logout(request):
    auth.logout(request)
    return redirect('profiles:user_login')
