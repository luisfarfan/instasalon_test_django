from rest_framework import serializers

from professional.models import Professional, ProfessionalService
from services.serializers import ServiceSerializer


class ProfessionalSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = Professional
        fields = '__all__'


class ProfessionalServiceSerializer(serializers.ModelSerializer):
    profesional = ProfessionalSerializer()
    service = ServiceSerializer()

    class Meta:
        model = ProfessionalService
        fields = '__all__'
