from django.urls import path
from .views import ReservationAPIView, keyApiView

urlpatterns = [
    path('reservations',ReservationAPIView.as_view, name='reservations'),
    path('keys', keyApiView.as_view, name='keys'),
]