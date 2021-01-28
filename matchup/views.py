from .serializers import GameListSerializer
from .models import GameList
from rest_framework import viewsets, generics


class GameListViewSet(viewsets.ModelViewSet):
    queryset = GameList.objects.all()
    serializer_class = GameListSerializer

    def get_queryset(self):
        return GameList.objects.all()