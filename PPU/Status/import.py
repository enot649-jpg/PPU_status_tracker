import pandas as pd
from django.core.management.base import BaseCommand
from .models import Sogl, Departure, Units, Act

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_excel('sogl.xlsx', sheet_name='Sheet1')

        for index, row in df.iterrows():
            dep = Departure.objects.get(id=row['departure_id'])
            unit = Units.objects.get(id=row['unit_id'])
            act = Act.objects.get(id=row['needs_act_id'])

            Sogl.objects.create(
                name=row['name'],
                status=row['status'],
                group=row['group'],
                dogovor=row['dogovor'],
                meropr=row['meropr'],
                payed=row['payed'],
                value=row['value'],
                departure=dep,
                unit=unit,
                needs_act=act
            )