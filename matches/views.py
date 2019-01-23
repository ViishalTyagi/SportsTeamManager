from django.shortcuts import render
from rest_framework import generics
from .models import Match
from .serializers import MatchSerializer

class MatchView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()