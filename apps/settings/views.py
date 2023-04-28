from django.shortcuts import render
from .models import Settings
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    context = {
        setting:'setting',
    }
    return render(request,'school/index.html',context)