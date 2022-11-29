from django.db import models

# Create your models here.

"""class Project(models.Model):
    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE, related_name='users')
    title = models.CharField(max_length=256)
    noOfPlayers = models.PositiveSmallIntegerField(blank=True)
    difficulty = models.CharField(max_length=10, blank=True)
    hasActor = models.BooleanField(blank=True)
    theme = models.CharField(max_length=256, blank=True)
    scenario = models.TextField(blank=True)
    noOfRiddles = models.PositiveSmallIntegerField(blank=True)"""