from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'name',
            'image',
            'city',
            'sport',
        ]

class TeamGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [
            'name',
            'image',
            'city',
            'sport',
            
        ]