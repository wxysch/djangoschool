from django.shortcuts import render, HttpResponse
from .models import Settings,Gallery
from apps.news.models import News
# Create your views here.
def index(request): 
    context = {
        'setting': Settings.objects.latest('id'),
        'news':News.objects.all(),
        'gallery':Gallery.objects.all()
        }
    return render(request,'school\index.html',context)

def about(request):
    return render(request,'school\about.html')