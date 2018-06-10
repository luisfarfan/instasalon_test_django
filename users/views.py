from rest_framework import viewsets

from users.models import Users
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
