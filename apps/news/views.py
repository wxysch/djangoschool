from django.shortcuts import render
from .models import News
from apps.settings.models import Settings
# Create your views here.
def news_details(request,id):
    settings = Settings.objects.latest('id')
    news = News.objects.get(id=id)
    context = {
    'setting': settings,
    'news': news
    }
    return render(request,'school/news.html',context)