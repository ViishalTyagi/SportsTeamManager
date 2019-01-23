from django.shortcuts import render
from rest_framework import generics
from .models import Match
from .serializers import MatchSerializer
import django_filters

class MatchView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()

class MatchCreate(generics.CreateAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()

class MatchGet(generics.ListAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()