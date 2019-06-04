from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)

    class Meta:
        model = Game
        fields = '__all__'
