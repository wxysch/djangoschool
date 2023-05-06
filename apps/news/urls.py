from django.urls import path
from .views import news_details

urlpatterns = [
    path('news-detail/<int:id>/',news_details,name='news_details'),
]