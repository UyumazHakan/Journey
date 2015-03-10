__author__ = 'Hakan Uyumaz'

import pytz
import datetime

from django import forms

from ..models import JourneyUser

from ..utils import generate_token


class JourneyUserCreationForm(forms.ModelForm):
    class Meta:
        model = JourneyUser
        fields =['name', 'surname', 'email', 'password',]

    def save(self, commit=True):
        user = super(JourneyUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.activation_key=generate_token()
        user.activation_expire_date=datetime.datetime.now(pytz.utc) + datetime.timedelta(2)
        if commit:
            user.save()
        return user