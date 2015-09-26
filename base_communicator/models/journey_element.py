__author__ = 'Hakan Uyumaz'

from django.db import models

from ..models import Note, Photo, Audio, Video, Journey


class JourneyElement(models.Model):
    TYPE_LABELS = (('N', 'NOTE'), ('P', 'PHOTO'), ('A', 'AUDIO'), ('V', 'VIDEO'))
    type = models.CharField(max_length=1, choices=TYPE_LABELS, null=False, blank=False)
    note = models.ForeignKey(Note)
    photo = models.ForeignKey(Photo)
    audio = models.ForeignKey(Audio)
    video = models.ForeignKey(Video)
    journey = models.ForeignKey(Journey, related_name="elements")
