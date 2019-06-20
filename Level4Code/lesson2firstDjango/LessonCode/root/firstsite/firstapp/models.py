from django.db import models

# Create your models here.


class Article(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.headline
