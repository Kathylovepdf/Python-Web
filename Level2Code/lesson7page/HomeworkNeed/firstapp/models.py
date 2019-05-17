from django.db import models
from faker import Factory


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


# f = open('C:/Users/xuetangx/Desktop/pictures.txt', 'r')
# fake = Factory.create()
# for url in f.readlines():
#     a = Article(
#         title=fake.text(max_nb_chars=90),
#         img=url,
#         content=fake.text(max_nb_chars=3000),
#         views=fake.pyint(),
#         likes=fake.pyint(),
#         createtime=fake.date_time(),
#         )
#     a.save()
