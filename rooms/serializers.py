from rest_framework import serializers

from professional.serializers import ProfessionalServiceSerializer
from rooms.models import Rooms, RoomProfessionalService


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'


class RoomProfessionalServiceSerializer(serializers.ModelSerializer):
    profesional_service = ProfessionalServiceSerializer()

    class Meta:
        model = RoomProfessionalService
        fields = '__all__'
