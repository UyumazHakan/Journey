__author__ = 'Hakan Uyumaz'

from django.contrib import admin
from ..models import JourneyUser

class JourneyUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Infromation',    {'fields': ['photo', 'name', 'surname']}),
        ('Contact information',     {'fields': ['email']}),
    ]


admin.site.register(JourneyUser, JourneyUserAdmin)