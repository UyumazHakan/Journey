__author__ = 'Hakan Uyumaz'

from django.contrib import admin

from .models import User, Journey, Education, Work, School, Company, Interest


class JourneyAdmin(admin.ModelAdmin):
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


admin.site.register(Journey, JourneyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Interest, InterestAdmin)