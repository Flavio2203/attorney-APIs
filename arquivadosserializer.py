from rest_framework import serializers
from arquivados.models import Arquivados

class ArquivadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivados
        fields = [
            'nomedoarquivo',
        ]
    
