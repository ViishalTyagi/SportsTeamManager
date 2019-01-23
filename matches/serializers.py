from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        fields = [
            'first_team',
            'second_team',
            'date_time',
            'location',
            'score',
        ]
        