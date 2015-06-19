__author__ = 'Hakan Uyumaz'

from django.db import models

from .user import User


class Friendship(models.Model):
    TYPE_LABELS = (('Fr', 'Friend'), ('Fo', 'Follower'))
    type = models.CharField('Friendship Type', max_length=50, choices=TYPE_LABELS)
    creation_date = models.DateField('Friendship Creation Date', null=False, blank=False, auto_now_add=True)
    owner = models.ForeignKey(User, related_name="Friendship Owner", null=False, blank=False)
    friend = models.ForeignKey(User, related_name="Friendship Friend", null=False, blank=False)
