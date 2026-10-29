from django.test import TestCase
from ..forms import NewForm
from ..models import Departure, Units, Act


class TestForms(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.departure = Departure.objects.create(departure='Департамент')
        cls.unit = Units.objects.create(unit='Подразделение')
        cls.needs_act = Act.objects.create(needs_act='Да')
        cls.form_data = {
            'name': '',
            'meropr': '1000-1000',
            'dogovor': 'АВ-тест1',
            'value': 1000.00,
            'payed': 100.00,
            'status': 'Тестовый Статус',
            'unit': cls.unit.pk,
            'group': 'Приобретение',
            'departure': cls.departure.pk,
            'needs_act': cls.needs_act.pk,
        }
    

    def test_validation(self):
        form = NewForm(data=self.form_data)
        self.assertFalse(form.is_valid())


