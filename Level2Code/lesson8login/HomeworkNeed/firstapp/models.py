
from django.db import models
from faker import Factory
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=500)
    avatar = models.CharField(max_length=250, default="static/images/default.png")
    comment = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)

    belong_to = models.ForeignKey(to=Article, related_name="under_comments", null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name="profile")
    profile_image = models.FileField(upload_to='profile_image')

# f = open('C:/Users/xuetangx/Desktop/pictures.txt', 'r')
# fake = Factory.create()
# for url in f.readlines():
#     a = Article(
#         title=fake.text(max_nb_chars=90),
#         img=url,
#         content=fake.text(max_nb_chars=1000),
#         views=fake.pyint(),
#         likes=fake.pyint(),
#         createtime=fake.date_time(),
#             )
#     a.save()
