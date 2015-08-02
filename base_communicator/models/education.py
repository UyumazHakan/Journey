__author__ = 'Hakan Uyumaz'

from django.db import models

from .school import School


class Education(models.Model):
    program = models.TextField(max_length=50, null=False, blank=False)
    school = models.ForeignKey(School, related_name='school')
    starting_date = models.DateField('Education Starting Date', null=True, blank=True, auto_now_add=False)
    ending_date = models.DateField('Education Ending Date', null=True, blank=True, auto_now_add=False)