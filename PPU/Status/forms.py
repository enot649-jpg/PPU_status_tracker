from django import forms
from .models import Sogl, Units, Departure, Act

class UnitForm(forms.Form):
    unit = forms.ModelChoiceField(
        queryset = Units.objects.all(),
        label = 'Ответственный за заполнение статуса',
        required = False,
        empty_label = '-'
    )


class InitForm(forms.Form):
    init = forms.ModelChoiceField(
        queryset = Units.objects.all(),
        label = 'Инициатор',
        required = False,
        empty_label = '-'
    )


class DepartureForm(forms.Form):
    departure = forms.ModelChoiceField(
        queryset=Departure.objects.all(),
        label='Стадия реализации',
        required=False,
        empty_label="-"
    )   
    

class ActForm(forms.Form):
    needs_act = forms.ModelChoiceField(
        queryset=Act.objects.all(),
        label='Необходима Актуализация',
        required=False,
        empty_label="-"
    )


class NewForm(forms.ModelForm):
    class Meta:
        model = Sogl
        fields = ('name', 'meropr', 'dogovor',
                  'value', 'payed', 'status',
                  'unit', 'init', 'group', 'departure', 'needs_act',
        )