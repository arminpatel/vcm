from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)
    username = models.CharField(max_length=128, blank=False, unique=True, null=False)
    cf_username = models.CharField(blank=True, null=True, max_length=256)
    at_username = models.CharField(blank=True, null=True, max_length=256)
    cc_username = models.CharField(blank=True, null=True, max_length=256)