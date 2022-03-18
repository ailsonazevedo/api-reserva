from django.urls import path
from .views import ChaveAPIView, ReservaAPIView


urlpatterns = [
    path('reservas/', ReservaAPIView.as_view(), name='reservas'),
    path('chaves/', ChaveAPIView.as_view(), name='chaves'),
]