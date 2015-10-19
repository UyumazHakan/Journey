__author__ = 'Hakan Uyumaz'

from django.db import models


class Photo(models.Model):
    title = models.TextField(max_length=50, null=True, blank=True)
    publish_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    edit_date = models.DateTimeField(null=False, blank=False, auto_now=True)
    photo = models.ImageField(upload_to='uploaded/journey/elements/photo/%Y/%m/%d/%H/', null=False,
                              blank=False)

    def __str__(self):
        return self.title + " " + str(self.publish_date)