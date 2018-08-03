from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    img = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    favs = models.IntegerField(default=0)
    createtime = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
