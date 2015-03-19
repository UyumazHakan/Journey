__author__ = 'Hakan Uyumaz'

from django.contrib import admin

class JourneyUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Infromation',    {'fields': ['photo', 'name', 'surname']}),
        ('Contact information',     {'fields': ['email']}),
    ]


