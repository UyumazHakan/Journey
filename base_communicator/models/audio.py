__author__ = 'Hakan Uyumaz'

from django.db import models


class Audio(models.Model):
    title = models.TextField(max_length=50, null=True, blank=True)
    publish_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    edit_date = models.DateTimeField(null=False, blank=False, auto_now=True)
    link = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return self.title + " " + self.publish_date