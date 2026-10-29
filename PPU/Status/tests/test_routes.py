import unittest
from django.test import TestCase
from ..models import Sogl, Departure, Units, Act
from django.urls import reverse
from rest_framework.test import APITestCase

class TestRotes(TestCase):
    def setUp(self):
        self.department = Departure.objects.create(departure='Департамент')
        self.unit = Units.objects.create(unit='Подразделение')
        self.act = Act.objects.create(needs_act='Нет')
        self.new_sogl = Sogl.objects.create(
            name='Тест',
            meropr='1',
            dogovor='1', 
            value=100, 
            payed=100,
            status='Тест',
            unit=self.unit, 
            group='Тест',
            departure=self.department, 
            needs_act=self.act
        )


class TestRoutes(TestCase):
    def testMainPageView(self):
        url = reverse('Status:sogl')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @unittest.expectedFailure
    def testEditPageView(self):
        url = reverse('Status:edit_sogl', args=(self.new_sogl.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class APITest(APITestCase):
    def testAPIreturn(self):
        response = self.client.get('/api/sogl/')
        self.assertEqual(response.status_code, 200)

    def testAPIreturnJson(self):
        response = self.client.get('/api/sogl/')
        self.assertIn('application/json', response['Content-Type'])