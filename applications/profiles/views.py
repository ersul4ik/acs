# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from applications.profiles.forms import FormProfile, FormLogin
from applications.profiles.models import Profile


def logout(request):
    auth.logout(request)
    return redirect('profiles:login')


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
    template = 'users_list.html'
    profiles_list = Profile.objects.filter()
    return render(request, template, {'profiles': profiles_list})


@login_required
def create_user(request):
    template = 'user/create_user.html'
    return render(request, template)


@login_required
def view_user(request, username):
    template = 'user_view.html'
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, template)


@login_required
def change_user(request, username):
    template = 'user/change_user.html'
    profile = get_object_or_404(Profile, user__username=username)
    form = FormProfile(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        form.save()
    return render(request, template, {
        'form': form,
        'profile': profile,
    })


@login_required
def change_password(request, username):
    template = 'user/change_password.html'
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, template)


@login_required
def change_permissions(request, username):
    template = 'user/change_permissions.html'
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, template)
