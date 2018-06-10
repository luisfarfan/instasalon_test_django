from rest_framework import serializers

from bookings.models import Bookings
from users.serializers import UserSerializer


class BookingSerializer(serializers.ModelSerializer):
    # room_profesional_service = ProfessionalServiceRoomSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    profesional_service_room_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Bookings
        fields = '__all__'
