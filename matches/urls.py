from django.urls import path
from .views import MatchView, MatchCreate

app_name='matches-api'

urlpatterns = [
    path('create',MatchCreate.as_view(), name='create-matches'),
    path('rud/<pk>/',MatchView.as_view(), name='matches'),
]