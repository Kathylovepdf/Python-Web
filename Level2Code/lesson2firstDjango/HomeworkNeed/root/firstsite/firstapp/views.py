from django.shortcuts import render
# Create your views here.


def index(request):
    index_page = render(request, 'list.html')
    return index_page
