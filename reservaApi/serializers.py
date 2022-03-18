from rest_framework import serializers
from .models import Reservation, Key


class ReservaSerializer(serializers.ModelSerializer):
    model = Reservation
    fields = '__all__'



class ChaveSerializer(serializers.ModelSerializer):
    model = Key
    fields = '__all__'
