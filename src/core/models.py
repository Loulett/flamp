# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def get_responses(self):
        return self.responses

    def get_comments(self):
        return self.comments
