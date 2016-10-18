# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    cards = models.ManyToManyField('cards.Card', related_name='categories')
