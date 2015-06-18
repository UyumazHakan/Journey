__author__ = 'Hakan Uyumaz'

from .user import UserAdmin
from .journey import JourneyAdmin
from ..models import Journey, User
from django.contrib import admin

admin.site.register(Journey, JourneyAdmin)
admin.site.register(User, UserAdmin)