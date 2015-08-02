__author__ = 'Hakan Uyumaz'

from django.db import models


class Company(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)