# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=300, unique=True)
    content=models.TextField()
