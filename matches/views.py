from django.shortcuts import render
from rest_framework import generics
from .models import Match
from teams.models import Team
from django.db.models import Q
from .serializers import MatchSerializer
from django_filters import rest_framework as filters
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class MatchView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()

class MatchCreate(generics.CreateAPIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()

class MatchFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="date_time", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="date_time", lookup_expr='lte')
    date_range = filters.DateRangeFilter(field_name='date_time')
    class Meta:
        model = Match
        fields = ('first_team', 'second_team', 'start_date', 'end_date', 'date_range',)


class MatchGet(generics.ListAPIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MatchFilter

    def get_queryset(self):
        qs = Match.objects.all()
        team_id = self.request.query_params.get('team', None)
        if team_id is not None:
            qs = qs.filter(Q(first_team=team_id) | Q(second_team=team_id))
        return qs