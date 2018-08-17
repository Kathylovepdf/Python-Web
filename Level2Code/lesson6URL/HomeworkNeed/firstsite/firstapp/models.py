from django.db import models

# Create your models here.
# class Article(models.Model):
#     headline = models.CharField(null=True, blank=True, max_length=100)
#     content = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.headline


class Comment(models.Model):
    name = models.CharField(max_length=10)
    avatar = models.CharField(max_length=100, default="/static/images/default.png")
    content = models.TextField()
    create_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
