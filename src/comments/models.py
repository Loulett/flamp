# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Comment(models.Model):
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey('core.User', related_name='comments')
    response = models.ForeignKey('responses.Response', related_name='comments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)