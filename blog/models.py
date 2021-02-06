from django.db import models
from django.utils import timezone


class Admin(models.Model):
    author = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title