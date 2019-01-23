from django.urls import path
from .views import TeamView, TeamCreate, TeamGet

app_name='teams-api'

urlpatterns = [
    path('create', TeamCreate.as_view(), name='create-teams'),
    path('rud/<pk>/', TeamView.as_view(), name='rud-teams'),
    path('<pk>/', TeamGet.as_view(), name='get-teams'),
]