__author__ = 'Hakan Uyumaz'

from .user import JourneyUserAdmin
from .journey import JourneyAdmin
from ..models import Journey, JourneyUser
from django.contrib import admin

admin.site.register(Journey, JourneyAdmin)
admin.site.register(JourneyUser, JourneyUserAdmin)