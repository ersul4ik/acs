# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from applications.accounts.forms import FormProfile, FormLogin
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
    user_list = User.objects.filter()
    return render(request, template, {'users': user_list})


@login_required
def create_user(request):
    template = 'user/create_user.html'
    return render(request, template)


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


@csrf_exempt
def api_create_user(request):
    """
    :request:
        finger_id

    :response:
        0 - Пользователь успешно создан
        1 - Такой пользователь уже есть
        2 - Не корректные параметры запроса
        3 - Не верный тип запроса
    """

    if request.method != 'POST':
        return HttpResponse(3)
    finger_id = request.POST.get('finger_id')

    if not finger_id:
        return HttpResponse(2)

    user, create = User.objects.get_or_create(id_finger=finger_id, username=finger_id)

    if not create:
        return HttpResponse(1)

    user.set_password(finger_id)
    user.is_active = False
    user.save()

    return HttpResponse(0)
