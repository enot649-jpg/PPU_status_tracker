from django import forms
from .models import Sogl, Units, Departure, Act

class UnitForm(forms.Form):
    unit = forms.ModelChoiceField(
        queryset = Units.objects.all(),
        label = 'Подразделение',
        required = False,
        empty_label = '-'
    )


class DepartureForm(forms.Form):
    departure = forms.ModelChoiceField(
        queryset=Departure.objects.all(),
        label='Департамент',
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
                  'unit', 'group', 'departure', 'needs_act',
        )