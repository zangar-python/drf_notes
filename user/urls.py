from django.urls import path
from .views import RegisterView,LoginView,UserDataViews

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('me/',UserDataViews.as_view())
]
