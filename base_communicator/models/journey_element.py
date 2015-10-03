__author__ = 'Hakan Uyumaz'

from django.db import models

from ..models import Note, Photo, Audio, Video, Journey


class JourneyElement(models.Model):
    TYPE_LABELS = (('N', 'NOTE'), ('P', 'PHOTO'), ('A', 'AUDIO'), ('V', 'VIDEO'))
    type = models.CharField(max_length=1, choices=TYPE_LABELS, null=False, blank=False)
    note = models.ForeignKey(Note, null=True, blank=True)
    photo = models.ForeignKey(Photo, null=True, blank=True)
    audio = models.ForeignKey(Audio, null=True, blank=True)
    video = models.ForeignKey(Video, null=True, blank=True)
    journey = models.ForeignKey(Journey, related_name="elements")
    index = models.IntegerField()

    def get_journey_element(self):
        type = self.type
        if type == 'N':
            return self.note
        elif type == 'P':
            return self.photo
        elif type == 'A':
            return self.audio
        elif type == 'V':
            return self.video

