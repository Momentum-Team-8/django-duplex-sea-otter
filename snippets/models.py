from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

