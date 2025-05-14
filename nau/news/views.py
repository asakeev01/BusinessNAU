from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import *


def index(request):
    latest_news = News.objects.filter(type='Latest').order_by('-id')
    upcoming_news = News.objects.filter(type='Upcoming').order_by('-id')
    config = NewsPageConfig.get_solo()
    context = {
        'latest_news': latest_news,
        'upcoming_news': upcoming_news,
        'config': config
    }
    return render(request, 'news/news_list.html', context)


def detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)
