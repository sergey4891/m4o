from django import forms

from .models import Order, Persons, Partner


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_name', 'department', 'location', 'vacancy', 'start_date', 'finish_date', 'start_time',
                    'finish_time', 'count_of_persons', 'dogovor', 'price_per_hour', 'price_for_user',
                    'responsible_full_name', 'status']


class AddPersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ['full_name', 'phone', 'date_of_birth', 'city', 'gender']


class AddPartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
            # ['name_legal_entity', 'ogrn', 'legal_address', 'inn', 'kpp', 'bank', 'p_s', 'k_s', 'bik']


class AddDogovorForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['num_end_date', 'sum_dogovor', 'services', 'status', 'legal_entity']