__author__ = 'Hakan Uyumaz'

from django.contrib import admin

from .user import UserAdmin
from .journey import JourneyAdmin
from ..models import Journey, User


admin.site.register(Journey, JourneyAdmin)
admin.site.register(User, UserAdmin)