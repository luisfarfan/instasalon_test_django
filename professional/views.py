from rest_framework import viewsets

from professional.models import Professional
from professional.serializers import ProfessionalSerializer


class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    permission_classes = ()
