__author__ = 'Hakan Uyumaz'

from django.db import models


class School(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    type = models.TextField(max_length=50, null=False, blank=False)