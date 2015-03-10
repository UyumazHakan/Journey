__author__ = 'Hakan Uyumaz'

from django.db import models
from .journey import Journey

class Note(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    text = models.TextField(max_length=1000, null=True, blank=True)
    journey = models.ForeignKey(Journey)