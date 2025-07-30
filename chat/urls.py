from django.urls import path
from .views import MessageListFromChat,ChatListView,MessageCreateView

urlpatterns = [
    path('chats/',ChatListView.as_view()),
    path('chats/<int:pk>/',MessageListFromChat.as_view()),
    path('chats/message/',MessageCreateView.as_view())
]
 