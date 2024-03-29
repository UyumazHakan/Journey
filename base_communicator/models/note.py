__author__ = 'Hakan Uyumaz'

from django.db import models


class Note(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False)
    publish_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    edit_date = models.DateTimeField(null=False, blank=False, auto_now=True)
    text = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title