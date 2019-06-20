from django.shortcuts import render, HttpResponse
from firstapp.models import Article
# from django.template import Context, Template

# Create your views here.


def index(request):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'first_web_2.html', context)
    return index_page
