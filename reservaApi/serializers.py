from rest_framework import serializers
from .models import Reservation, Key


class ReservaSerializer(serializers.ModelSerializer):
    model = Reservation
    fields = [
        'first_name',
        'last_name',
        'date_reservation',
        'reservation'
        ]



class ChaveSerializer(serializers.ModelSerializer):
    model = Key
    fields = ['nome','numero']
