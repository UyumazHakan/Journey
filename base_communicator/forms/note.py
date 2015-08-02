__author__ = 'Hakan Uyumaz'

import datetime

import pytz
from django import forms

from ..models import Note


class NoteCreationForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']

    def save(self, commit=True):
        note = super(NoteCreationForm, self).save(commit=False)
        note.date = datetime.datetime.now(pytz.utc)
        if commit:
            note.save()
        return note