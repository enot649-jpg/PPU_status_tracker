from rest_framework import serializers
from .models import Sogl, History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = (
        'id', 'status', 'payed', 'date',
        )

class SoglSerializer(serializers.ModelSerializer):
    history = HistorySerializer(many=True)
    class Meta:
        model = Sogl
        fields = (
        'id', 'name', 'modified_at', 'meropr', 'dogovor',
        'value', 'payed', 'status',
        'unit', 'group', 'departure', 'needs_act', 'history',
        )

