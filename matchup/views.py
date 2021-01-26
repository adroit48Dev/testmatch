from django.shortcuts import render
from .serializers import MatchContentSerializer, MatchModelSerializer, EntrySerializer
from .models import MatchContent, MatchModel, Entry
from rest_framework import viewsets, generics


# Create your views here.
class MatchContentViewSet(viewsets.ModelViewSet):
    queryset = MatchContent.objects.all()
    serializer_class = MatchContentSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

#7871743518
# class MatchupGameViewSet(viewsets.ModelViewSet):
#     queryset = MatchContent.objects.all()
#     serializer_class = AllSerializer