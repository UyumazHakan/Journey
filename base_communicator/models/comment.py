__author__ = 'Hakan Uyumaz'

from django.db import models

from .journey import Journey
from .user import User


class Comment(models.Model):
    publish_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    edit_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    journey = models.ForeignKey(Journey, related_name='comments')
    user = models.ForeignKey(User, related_name='comments')
    loves = models.ManyToManyField(User, related_name='comment_loves')

    def __str__(self):
        return self.text