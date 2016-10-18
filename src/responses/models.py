# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Response(models.Model):
    text = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField()  # from 1 to 5
    author = models.ForeignKey('core.User', related_name='responses')
    card = models.ForeignKey('cards.Card', related_name='responses', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_comments(self):
        return self.comments

