from django.shortcuts import render
from .serializers import GameListSerializer
from .models import GameList
from rest_framework import viewsets, generics

#
# # Create your views here.
# class MatchContentViewSet(viewsets.ModelViewSet):
#     queryset = MatchContent.objects.all()
#     serializer_class = MatchContentSerializer
#
#
# class EntryViewSet(viewsets.ModelViewSet):
#     queryset = Entry.objects.all()
#     serializer_class = EntrySerializer
#
# #7871743518
# # class MatchupGameViewSet(viewsets.ModelViewSet):
# #     queryset = MatchContent.objects.all()
# #     serializer_class = AllSerializer
#
# class PortfolioViewSet(viewsets.ModelViewSet):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer

class GameListViewSet(viewsets.ModelViewSet):
    queryset = GameList.objects.all()
    serializer_class = GameListSerializer

    def get_queryset(self):
        return GameList.objects.all()