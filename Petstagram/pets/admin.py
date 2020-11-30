from django.contrib import admin

from pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    admin.site.register(Pet)
