__author__ = 'Hakan Uyumaz'

from django.db import models

from .company import Company


class Work(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, related_name='company')