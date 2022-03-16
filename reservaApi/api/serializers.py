from reservaApi.models import Reservation
from rest_framework import serializers
from ..models import *

class ReservaSerializers(serializers.ModelSerializer):
    model = Reservation
    filed = "__all__"
