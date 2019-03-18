# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import ListView

from .forms import PostForm

# Create your views here.
from django.urls import reverse

from django.shortcuts import render
from .models import Post


def post(request):
    if request.method == 'POST':
        data = Post.objects.all()   #wyswietlenie danych z bazy
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            post_obj = Post(title = title, content = content)
            post_obj.save()

    else:
        form = PostForm()


    return render(request, 'databaseform2.html', {'data': data})

