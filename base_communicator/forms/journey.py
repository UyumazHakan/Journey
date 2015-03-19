__author__ = 'Hakan Uyumaz'

import pytz
import datetime

from django import forms

from ..models import Journey

class JourneyCreationForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields =['title']

    def save(self, commit=True):
        journey = super(JourneyCreationForm, self).save(commit=False)
        journey.date=datetime.datetime.now(pytz.utc)
        if commit:
            journey.save()
        return journey