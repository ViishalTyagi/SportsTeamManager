from django.urls import path
from .views import TeamView

app_name='teams-api'

urlpatterns = [
    path('<pk>/', TeamView.as_view(), name='teams')
]