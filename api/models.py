from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Person(AbstractUser):
    reset_token = models.CharField(max_length=32, blank=True)
    remember_at = models.DateTimeField(null=True)
    email_verified_at = models.DateTimeField(null=True)
    clients_table = models.TextField(blank=True)
    events_table = models.TextField(blank=True)
    attendees_table = models.TextField(blank=True)
