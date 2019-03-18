# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

# Create your views here.


def index(request):
    text = {'mytext': 'abcdf'}
    return render(request, 'index.html', text)


class PostView(View):

    def get(self, request):
        return render(request, "formfile.html")

    def post(self, request):
        ctx = {}
        if 'q' in request.POST:
            ctx['rlt'] = request.POST['q']
        else:
            ctx['rlt2'] = request.POST['qq']
        return render(request, "formfile.html", ctx)

