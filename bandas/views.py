from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Banda, Genero
from .serializers import BandaSerializer, GeneroSerializer


class SaludoView(APIView):
    def get(self, request):
        return Response({"mensaje": "Bienvenidos al taller de Django y Django REST Framework"})


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class BandaViewSet(viewsets.ModelViewSet):
    queryset = Banda.objects.select_related('genero').all()
    serializer_class = BandaSerializer