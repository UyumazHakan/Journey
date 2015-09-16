__author__ = 'Hakan Uyumaz'

from django.db import models

from .user import User


class Journey(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False)
    position = models.TextField(max_length=50, null=True, blank=True)
    category = models.TextField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='uploaded/journey/photos/%Y/%m/%d/%H/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='uploaded/static/journey/cover_photos/%Y/%m/%d/%H/', null=True,
                                    blank=True)
    date = models.DateField(null=False, blank=False)
    summary = models.TextField(max_length=1000, null=True, blank=True)
    users = models.ManyToManyField(User, related_name="journeys", )
    owner = models.ForeignKey(User, related_name="owned_journeys")
    sharers = models.ManyToManyField(User, related_name="shared_journeys")
    loves = models.ManyToManyField(User, related_name='journey_loves')
    def __str__(self):
        return self.title