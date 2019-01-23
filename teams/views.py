from django.shortcuts import render
from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer

class TeamView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()