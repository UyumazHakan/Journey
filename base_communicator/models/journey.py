__author__ = 'Hakan Uyumaz'

from django.db import models

from .user import User


class Journey(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False)
    cover_photo = models.ImageField(upload_to='web/static/journey_photos/%Y/%m/%d/%h/', null=True, blank=True)
    date = models.DateField(null=False, blank=False)
    summary = models.TextField(max_length=1000, null=True, blank=True)
    users = models.ManyToManyField(User, related_name="users", )
    owner = models.ForeignKey(User, related_name="owner")

    def __str__(self):
        return self.title