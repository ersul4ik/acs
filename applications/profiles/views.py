# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from applications.profiles.forms import FormProfile, FormLogin
from applications.profiles.models import Profile


def logout(request):
    auth.logout(request)
    return redirect('profiles:user_login')


def login(request):
    template = 'login.html'
    form = FormLogin(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect(request.GET.get('next') or '/')
    return render(request, template, {'form': form})


@login_required
def user_list(request):
    pass


@login_required
def create_user(request):
    pass


@login_required
def view_user(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    pass


@login_required
def change_user(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    form = FormProfile(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        form.save()
    return render(request, 'profile.html', {
        'form': form,
        'profile': profile,
    })


@login_required
def change_password(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    pass


@login_required
def change_permissions(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    pass
