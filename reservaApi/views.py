from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation, Key
from .serializers import ReservaSerializer, ChaveSerializer


class ReservaAPIView(APIView):

    """
    Api de reservas
    """
    def get(self, request):
        reservas = Reservation.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)


class ChaveAPIView(APIView):

    """
    Api de chaves
    """
    def get(self, request):
        chaves = Key.objects.all()
        serializer = ChaveSerializer(chaves, many=True)
        return Response(serializer.data)
# Create your views here.

