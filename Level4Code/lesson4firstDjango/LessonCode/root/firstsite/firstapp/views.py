from django.shortcuts import render, HttpResponse
from firstapp.models import Article
import MySQLdb
# from django.template import Context, Template
# Create your views here.


def index(request):
    coon = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='django4',
        charset='utf8'
    )

    cursor = coon.cursor()
    cursor.execute('select * from firstapp_article')
    # count = cursor.execute('select * from firstapp_article')
    # print(count)
    results = cursor.fetchall()
    # print(results)
    article_list = []
    for result in results:
        article_list.append(
            {
                'title': result[1],
                'content': result[2]
            }
        )
    # print(article_list)
    context = {}
    context['article_list'] = article_list
    return render(request, 'first_web_2.html', context)
