from django.shortcuts import render, HttpResponse
from firstapp.models import Article
# Create your views here.


def index(request):
	article_list = Article.objects.all()
	context = {}
	context['article_list'] = article_list
	index_page = render(request, 'index.html', context)
	return index_page
