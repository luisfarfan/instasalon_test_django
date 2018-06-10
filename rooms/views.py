from rest_framework import viewsets

from rooms.models import Rooms
from rooms.serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    permission_classes = ()
