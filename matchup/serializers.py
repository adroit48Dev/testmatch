from rest_framework import serializers
from .models import GameList



class GameListSerializer(serializers.ModelSerializer):
    keyword = serializers.ListField(child=serializers.CharField())
    img_key = serializers.ListField(child=serializers.FileField(blank=True))
    definition = serializers.ListField(child=serializers.CharField(max_length=500))
    mat_name = serializers.CharField()

    class Meta:
        fields= '__all__'
        model = GameList