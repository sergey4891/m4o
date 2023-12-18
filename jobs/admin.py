from django.contrib import admin
from .models import Persons, Partner, Order, Dogovor


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'date_of_birth', 'city', 'gender']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name_legal_entity', 'ogrn', 'legal_address', 'inn', 'kpp', 'bank', 'p_s', 'k_s', 'bik']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'department', 'location', 'vacancy', 'start_date', 'finish_date', 'start_time',
                    'finish_time', 'count_of_persons', 'dogovor', 'price_per_hour', 'price_for_user',
                    'responsible_full_name', 'status']


@admin.register(Dogovor)
class DogovorAdmin(admin.ModelAdmin):
    list_display = ['num_end_date', 'sum_dogovor', 'services', 'status', 'legal_entity']