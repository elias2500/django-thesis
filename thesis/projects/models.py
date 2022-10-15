from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE, related_name='users')
    title = models.CharField(max_length=256)
    noOfPlayers = models.PositiveSmallIntegerField(blank=True)
    difficulty = models.CharField(max_length=10, blank=True)
    hasActor = models.BooleanField(blank=True)
    theme = models.CharField(max_length=256, blank=True)
    scenario = models.TextField(blank=True)
    noOfRiddles = models.PositiveSmallIntegerField(blank=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__ (self):
        return self.user.username
