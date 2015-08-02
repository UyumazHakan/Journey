__author__ = 'Hakan Uyumaz'

from django.contrib import admin


class JourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_photo', 'summary', 'date', 'owner')
    fieldsets = [
        ('General Information', {'fields': ['title', 'cover_photo', 'summary', 'date', 'owner']}),
    ]


