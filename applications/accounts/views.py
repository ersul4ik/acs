# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from applications.accounts.forms import ProfileForm, LoginForm
from applications.accounts.models import User


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


def login(request):
    template = 'login.html'
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect(request.GET.get('next') or '/')
    return render(request, template, {'form': form})


@login_required
def account_list(request):
    template = 'account_list.html'
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users = User.objects.filter(
            is_active=True, position__departament=request.user.get_departament()
        ).exclude(position__departament=None).exclude(username=None)
    return render(request, template, {'account_list': users.order_by('-date_joined')})


@login_required
def change_user(request, username):
    template = 'account_view.html'
    user = get_object_or_404(User, username=username)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, template, {
        'form': form,
        'administrate': user,
    })
