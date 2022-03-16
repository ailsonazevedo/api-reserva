from reservaApi.models import Reservation
from rest_framework import viewsets
from .serializers import ReservaSerializers
from ..models import *

class ReservaViewsets(viewsets.ModelViewSet):
    class Meta:
        model = Reservation
        fields = "__all__"

