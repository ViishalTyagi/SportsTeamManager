from django.db import models
from teams.models import Team
from django.db.models import Q

class MatchManager(models.Manager):
    def search(self, query):
        lookups = (
            Q(first_team__iexact=query) | Q(second_team__iexact=query)
        )
        return self.objects.filter(lookups)

class Match(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team_1")
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team_2")
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=120)
    score = models.CharField(max_length=150, null=True, blank=True)
    objects = MatchManager()

    class Meta:
        verbose_name_plural = "Matches"
