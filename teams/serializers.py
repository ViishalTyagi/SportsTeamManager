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

    def validate_name(self, value):
        qs = Team.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Team already exists.")
        return value