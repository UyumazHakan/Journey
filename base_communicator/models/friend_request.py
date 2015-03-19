__author__ = 'Hakan Uyumaz'

from django.db import models

from .user import JourneyUser


class FriendshipRequest(models.Model):
    STATUS_LABELS = (('P', 'Pending'), ('D', 'Declined'), ('A', 'Accepted'))
    status = models.CharField('Status', max_length=50, choices=STATUS_LABELS)
    date = models.DateField('Date', null=False, blank=False)
    sender = models.ForeignKey(JourneyUser, related_name="sender")
    receiver = models.ForeignKey(JourneyUser, related_name="receiver")
