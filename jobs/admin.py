from django.contrib import admin
from .models import Persons, Partner


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    fields = ['full_name', 'phone']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ['name_legal_entity', 'phone']