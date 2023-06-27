from rest_framework import serializers
from processo.models import processo

class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = processo
        fields = [
            'periodotempo',
            'contagemencadeamento ',
            'tipoprocesso',
        ]