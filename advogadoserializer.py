from rest_framework import serializers
from advogado.models import Advogado

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = [
            'nome',
            'idade', 
            'genero'
            'telefone',
        ]
    
