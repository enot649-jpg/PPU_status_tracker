from django.test import TestCase
from ..models import Sogl, Departure, Units, Act

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.department = Departure.objects.create(departure='Департамент')
        cls.unit = Units.objects.create(unit='Подразделение')
        cls.needs_act = Act.objects.create(needs_act='Нет')
        for index in range(1, 11):
            Sogl.objects.create(
                name=f'Тестовое Имя {index}',
                meropr='1000-1000',
                dogovor='АВ-тест1',
                value=1000.00,
                payed=100.00,
                status=f'Тестовый Статус {index}',
                unit=cls.unit,
                group='Приобретение',
                departure=cls.department,
                needs_act=cls.needs_act,
            )

    def test_creation(self):
        count = Sogl.objects.count()
        self.assertEqual(count, 10)

    def test_payed(self):
        test = Sogl.objects.all()[0]
        self.assertEqual(test.payed, 100.00)

    def test_modified_at_addition(self):
        test = Sogl.objects.all()[0]
        self.assertIsNotNone(test.modified_at)