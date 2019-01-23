import datetime
from rest_framework import generics
from django.db.models import Q
from .models import Team
from matches.models import Match
from matches.serializers import MatchSerializer
from .serializers import TeamSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.utils import timezone
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class TeamView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()

class TeamCreate(generics.CreateAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()

class TeamGet(ObjectMultipleModelAPIView, generics.ListAPIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'
    
    def get_querylist(self):
        pk=self.kwargs.get('pk')
        time= timezone.now()
        querylist = [
        {'queryset': Team.objects.filter(pk=pk), 'serializer_class': TeamSerializer},
        {'queryset': Match.objects.filter(
            Q(date_time__gt=timezone.now()), Q(first_team=pk) | Q(second_team=pk)
            ).order_by('date_time'), 'serializer_class': MatchSerializer},
        ]  
        return querylist