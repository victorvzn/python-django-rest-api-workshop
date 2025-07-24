from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SaludoView
from .views import BandaViewSet
from .views import GeneroViewSet

router = DefaultRouter()
router.register(r'bandas', BandaViewSet)
router.register(r'generos', GeneroViewSet)

urlpatterns = [
    path('saludo/', SaludoView.as_view()),
    
    path('', include(router.urls)),
]