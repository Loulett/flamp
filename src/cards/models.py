# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField()
    rating = models.FloatField()

    def get_responses(self):
        return self.responses
