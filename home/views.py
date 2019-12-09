from rest_framework import viewsets

from home.models import Room
from home.serializers import RoomListSerializer, RoomDetailSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomListSerializer
        if self.action == 'retrieve':
            return RoomDetailSerializer
        return RoomListSerializer
