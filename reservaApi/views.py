from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Reservation, Key
from .serializers import ReservationSerializer, KeySerializer

class ReservationAPIView(APIView):
    """
    Api reservas
    """
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class KeyAPIView(APIView):
    """
    Api Chaves
    """
    def get(self, request):
        keys = Key.objects.all()
        serializer = KeySerializer(keys, many=True)
        return Response(serializer.data)
