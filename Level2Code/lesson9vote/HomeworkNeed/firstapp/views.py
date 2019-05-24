from django.shortcuts import render, redirect, Http404, HttpResponse
from firstapp.models import Article, Comment, Ticket
from firstapp.forms import CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
# from django.website.form import LoginForm

# Create your views here.


def index(request):
    article_list = Article.objects.all()

    page_robot = Paginator(article_list, 6)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
        # raise Http404
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context = {}
    context["article_list"] = article_list

    return render(request, 'index.html', context)


def detail(request, id):
    context = {}
    article = Article.objects.get(id=id)
    form = CommentForm
    # like_counts = Ticket.objects.filter(choice='like', article_id=id).count()
    # if request.method == "GET":

    try:
        voter_id = request.user.profile.id
        user_ticket_for_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        context['user_ticket_for_article'] = user_ticket_for_article
    except:
        pass
    context["article"] = article
    context['form'] = form

    # context['like_counts'] = like_counts

    return render(request, 'detail.html', context)


def vote(request, id):
    if not isinstance(request.user, User):
        return redirect(to='detail', id=id)

    voter_id = request.user.profile.id
    # print(request.POST)
    try:
        user_ticket_for_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_article.choice = request.POST['vote']
        user_ticket_for_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=id, choice=request.POST['vote'])
        new_ticket.save()

    if request.POST['vote'] == 'like':
        article = Article.objects.get(id=id)
        article.likes += 1
        article.save()

    return redirect(to='detail', id=id)


def comment(request, id):

    # if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        comment = form.cleaned_data["comment"]
        article = Article.objects.get(id=id)
        c = Comment(name=name, comment=comment, belong_to=article)
        c.save()
        return redirect(to="detail", id=id)
    return redirect(to="detail", id=id)


def index_login(request):
    context = {}
    if request.method == 'GET':
        # form = LoginForm
        form = AuthenticationForm

    if request.method == "POST":
        # form = LoginForm(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(username=username, password=password)
            # if user:
                # login(request, user)
            # else:
            #     return HttpResponse('<h1>Not a User</h1>')
            login(request, form.get_user())
            return redirect(to="index")
    context['form'] = form
    return render(request, 'login.html', context)


def index_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    context['form'] = form
    return render(request, 'register.html', context)

    # if request.method == "GET":
    #     form = UserCreationForm
    #
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(to='login')
    #
    # context = {}
    # context['form'] = form
    #
    # return render(request, 'register.html', context)
