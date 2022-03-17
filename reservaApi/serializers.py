from rest_framework import serializers
from .models import Reservation, Key

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        field = "__all__"


class keySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        field = "__all__"

