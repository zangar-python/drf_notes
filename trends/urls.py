from django.urls import path
from .views import TrendListCreate,TrendDetailView,TrendNewsListViews,BotCommandSys

urlpatterns = [
    path('trend/',TrendListCreate.as_view()),
    path('trend/<int:pk>/',TrendDetailView.as_view()),
    path('news/',TrendNewsListViews.as_view()),
    path('bot/',BotCommandSys.as_view())
]