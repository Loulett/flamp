from __future__ import unicode_literals
from django.db import models


class Like(models.Model):
    rating = models.PositiveIntegerField(default=0)
    response = models.ForeignKey('responses.Response')
