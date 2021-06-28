from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    ## favorite fields
    favorited_by = models.ManyToManyField("User", related_name="fav_snippets")
