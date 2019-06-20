from django.shortcuts import render, redirect

from firstapp.models import Article, Comment, Ticket, UserProfile
from firstapp.forms import CommentForm, UserProfileForm

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.
def collection(request):
    context = {}
    Tickets_like = Ticket.objects.filter(choice='like', voter=request.user)
    article_like_list=[ticket.article for ticket in Tickets_like]

    page_robot = Paginator(article_like_list, 3)
    page_num = request.GET.get('page')
    try:
        article_like_list = page_robot.page(page_num)
    except EmptyPage:
        article_like_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_like_list = page_robot.page(1)
    context['article_like_list'] = article_like_list
    return render(request, 'mycollection.html', context)


def profile(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == 'GET':
            form = UserProfileForm()


        if request.method == 'POST':
            try:
                request.user.profile.delete()
            except ObjectDoesNotExist:
                pass
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                sex = form.cleaned_data["sex"]
                avatar = form.cleaned_data["avatar"]
                name = form.cleaned_data["name"]
                b = UserProfile(name=name, sex=sex, avatar=avatar, belong_to=request.user)
                b.save()
                passwd = request.POST.get('password')
                if passwd:
                    request.user.set_password(passwd)
                    request.user.save()
                    logout(request)
                    return redirect(to='login')
                else:
                    print('啥也不干，因为没接收到密码')
                return redirect(to="profile")

        context['form'] = form
        return render(request, 'myinfo.html', context)
    else:
        return redirect(to="index")

def index(request):

    article_list = Article.objects.all()

    page_robot = Paginator(article_list, 5)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context = {}
    context["article_list"] = article_list

    return render(request, 'index.html', context)

def detail(request, id, error_form=None):
    article = Article.objects.get(id=id)

    if request.method == "GET":
        form = CommentForm
    context = {}
    context["article"] = article

    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form

    voter_id = request.user.id
    article.likes = Ticket.objects.filter(choice='like', article_id=id).count()
    try:
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, article_id=id)
        context['user_ticket'] = user_ticket_for_this_video
    except:
        pass

    context['article.likes'] = article.likes

    return render(request, 'detail.html', context)

def comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            c = Comment(comment=comment, belong_to_id=id, commenter_id=request.user.id)
            c.save()
            return redirect(to="detail", id=id)
        else:
            return detail(request, id, error_form=form)
    return redirect(to="detail", id=id)

def index_login(request):
    if request.method == "GET":
        form = AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index")

    context = {}
    context['form'] = form

    return render(request, 'login.html', context)

def index_register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form

    return render(request, 'register.html', context)

def vote(request, id):
    # 未登录用户不允许投票，自动跳回详情页

    if not isinstance(request.user, User):
        return redirect(to="detail", id=id)

    voter_id = request.user.id

    try:
        # 如果找不到登陆用户对此篇文章的操作，就报错
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_this_article.choice = request.POST["vote"]
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=id, choice=request.POST["vote"])
        new_ticket.save()

    # 如果是点赞，更新点赞总数
    # if request.POST["vote"] == "like":
    #     article = Article.objects.get(id=id)
    #     article.likes += 1
    #     article.save()

    return redirect(to="detail", id=id)
