from django.shortcuts import render, redirect
from firstapp.models import Comment
from firstapp.form import CommentForm
# Create your views here.


def detail(request):
    if request.method == "GET":
        form = CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST)
        # print(form)
        # print(form.errors)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            c = Comment(name=name, content=content)
            c.save()
            return redirect(to="detail")
    context = {}
    comment_list = Comment.objects.all()
    context['comment_list'] = comment_list
    context['form'] = form

    return render(request, 'detail.html', context)
