__author__ = 'Hakan Uyumaz'

from django.contrib import admin

from .models import User, Journey, JourneyElement, Education, Work, School, Company, Interest, Comment, Note, Photo, \
    Audio, Video


class JourneyAdmin(admin.ModelAdmin):
    pass


class JourneyElementAdmin(admin.ModelAdmin):
    pass

class NoteAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


class AudioAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    pass


class WorkAdmin(admin.ModelAdmin):
    pass


class SchoolAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


class InterestAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Journey, JourneyAdmin)
admin.site.register(JourneyElement, JourneyElementAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Comment, CommentAdmin)