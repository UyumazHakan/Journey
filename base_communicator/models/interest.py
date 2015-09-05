__author__ = 'Hakan Uyumaz'

from django.db import models


class Interest(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name