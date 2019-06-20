from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


# class UserProfile(models.Model):
#     belong_to = models.OneToOneField(to=User, null=True)
#     name = models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.name


class Article(models.Model):

    title = models.CharField(max_length=500, null=True)
    # author = models.ForeignKey(to=UserProfile, related_name="articles", null=True, default='Kathy')
    img = models.CharField(max_length=250, null=True)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    score = models.FloatField(default=1.1)
    likes = models.IntegerField(default=0)
    createtime = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
