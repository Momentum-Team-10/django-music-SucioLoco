from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class albums(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
# Create your models here.
