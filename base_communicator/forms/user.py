__author__ = 'Hakan Uyumaz'

from django import forms

from ..models import JourneyUser


class JourneyUserCreationForm(forms.ModelForm):

    class Meta:
        model = JourneyUser
        fields =['username', 'name', 'surname', 'email', 'password',]