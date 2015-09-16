__author__ = 'Hakan Uyumaz'

from django.db import models

from .journey import Journey
from .user import User


class Comment(models.Model):
    date = models.DateField(null=False, blank=False)
    text = models.TextField(max_length=1000, null=True, blank=True)
    journey = models.ForeignKey(Journey, related_name='comments')
    user = models.ForeignKey(User, related_name='comments')

    def __str__(self):
        return self.text