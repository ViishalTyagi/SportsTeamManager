from django.urls import path
from .views import MatchView

app_name='matches-api'

urlpatterns = [
    path('<pk>/',MatchView.as_view(), name='matches')
]