__author__ = 'Hakan Uyumaz'

from django.db import models

from .user import User


class FriendshipRequest(models.Model):
    STATUS_LABELS = (('P', 'Pending'), ('D', 'Declined'), ('A', 'Accepted'))
    status = models.CharField('Status', max_length=50, choices=STATUS_LABELS)
    date = models.DateField('Date', null=False, blank=False, auto_now_add=True)
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="receiver")

    def __str__(self):
        return 'Sender: ' + str(self.sender) + '\nReceiver: ' + str(self.receiver) + '\nStatus: ' + self.status