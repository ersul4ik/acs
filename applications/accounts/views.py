# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from applications.accounts.forms import FormProfile, FormLogin, FormCreateAccount
from applications.accounts.models import User


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


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
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users = User.objects.filter(
            is_active=True, position__departament=request.user.get_departament()
        ).exclude(position__departament=None).exclude(username=None)
    return render(request, template, {'user_list': users.order_by('-date_joined')})


@login_required
def create_user(request):
    template = 'user/create_user.html'
    form = FormCreateAccount(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = form.cleaned_data['is_active']
            user.is_staff = form.cleaned_data['is_staff']
            user.save()
    return render(request, template, {'form': form})


@login_required
def view_user(request, username):
    template = 'user_view.html'
    user = get_object_or_404(User, username=username)
    return render(request, template)


@login_required
def change_user(request, username):
    template = 'user/change_user.html'
    user = get_object_or_404(User, username=username)
    form = FormProfile(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        form.save()
    return render(request, template, {
        'form': form,
        'user': user,
    })


@login_required
def change_password(request, username):
    template = 'user/change_password.html'
    user = get_object_or_404(User, username=username)
    return render(request, template)


@login_required
def change_permissions(request, username):
    template = 'user/change_permissions.html'
    user = get_object_or_404(User, username=username)
    return render(request, template)
