from django.shortcuts import render, HttpResponse
from firstapp.models import Article
# from django.template import Context, Template

# Create your views here.


def index(request):
    context = {}
    # article_list = Article.objects.order_by('likes')正序

    # page = int(request.GET["page"])
    # article_list = Article.objects.all()[page-1:page]

    q = request.GET.get("q", "")
    article_list = Article.objects.filter(title__contains='q')

    print("sql: %s" % article_list.query)

    context['article_list'] = article_list
    return render(request, 'first_web_2.html', context)
