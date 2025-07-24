from rest_framework import serializers
from .models import Banda, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre']

class BandaSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer(read_only=True)
    genero_id = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(),
        source='genero',
        write_only=True
    )
    class Meta:
        model = Banda
        fields = ['id', 'nombre', 'genero', 'genero_id', 'portada']