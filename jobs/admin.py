from django.contrib import admin
from .models import Persons, Partner


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'date_of_birth', 'city', 'gender']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ['name_legal_entity', 'phone']