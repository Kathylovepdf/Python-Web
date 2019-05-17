from django.shortcuts import render, Http404
from firstapp.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    article_list = Article.objects.all()
    context = {}
    page_robot = Paginator(article_list, 6)
    page_num = request.GET.get('page')
    # print(type(page_num))
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
        # raise Http404
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context["article_list"] = article_list
    return render(request, 'index.html', context)
