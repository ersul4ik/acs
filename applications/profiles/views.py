# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from applications.profiles.forms import FormProfile


def create_profile(request):
    form = FormProfile(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form_valid = form.save(commit=False)  # не сохраняем заполненую форму

            form_valid.save()
        else:
            return render(request, "profile.html", {})

    return render(request, "profile.html", {'form': form})
