import datetime
from rest_framework import serializers

from bookings.models import Bookings, BookingState
from instasalon_test.const import BOOKINGSTATE
from rooms.serializers import RoomProfessionalServiceSerializer
from users.serializers import UserSerializer


class BookingStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingState
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    room_profesional_service = RoomProfessionalServiceSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    room_profesional_service_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    estado = BookingStateSerializer(read_only=True)
    estado_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Bookings
        fields = '__all__'

    def validate(self, data):
        reservas = Bookings.objects.filter(fecha=data['fecha'], estado=BOOKINGSTATE.ESPERA.value,
                                           room_profesional_service_id=data['room_profesional_service_id'],
                                           hora_inicio=data['hora_inicio'], hora_fin=data['hora_fin'])
        if reservas.count():
            raise serializers.ValidationError("Reserva no disponible")

        return data
