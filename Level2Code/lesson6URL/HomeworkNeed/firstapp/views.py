
from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import Article, Comment
from django.template import Context, Template
from firstapp.form import CommentForm
# Create your views here.


def index(request):
	article_list = Article.objects.all()
	context = {}
	context['article_list'] = article_list
	return render(request, 'index.html', context)


# def detail_old(request, page_num):
#
# 	if request.method == "GET":
#
# 	if request.method == "POST":
# 		form = CommentForm(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data["name"]
# 			content = form.cleaned_data["content"]
# 			a = Article.objects.get(id=page_num)
# 			c = Comment(name=name, content=content, belong_to=a)
# 			c.save()
# 			return redirect(to="detail", page_num=page_num)


def detail(request, page_num, error_form=None):
	form = CommentForm
	context = {}
	a = Article.objects.get(id=page_num)
	best_comment = Comment.objects.filter(belong_to=a, best_comment=True)
	# comment_list = Comment.objects.all()
	article = Article.objects.get(id=page_num)
	context['article'] = article
	if best_comment:
		context['best_comment'] = best_comment[0]
	# context['comment_list'] = comment_list
	if error_form is not None:
		context['form'] = error_form
	else:
		context['form'] = form

	return render(request, 'detail.html', context)


def detail_comment(request, page_num):
	form = CommentForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data["name"]
		content = form.cleaned_data["content"]
		a = Article.objects.get(id=page_num)
		c = Comment(name=name, content=content, belong_to=a)
		c.save()
	else:
		return detail(request, page_num, error_form=form)

		return redirect(to="detail", page_num=page_num)
