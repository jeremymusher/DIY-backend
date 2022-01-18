from cgitb import text
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = models.TextField()
    video_url = models.TextField()

    def __str__(self):
        return self.title