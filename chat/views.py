from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .botV1 import BotV1
from .models import Chat,Message
from .serializator import ChatSerializer,MessageSerializer

class ChatListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request:Request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats,many=True)
        return Response(data=serializer.data)
    def post(self,request:Request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class MessageListFromChat(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        chat = get_object_or_404(Chat,pk=pk)
        messages = chat.messages.all()
        serializer = MessageSerializer(messages,many=True)
        return Response(data=serializer.data)
    def delete(self,request:Request,pk):
        chat = get_object_or_404(Chat,pk=pk)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request:Request,pk):
        chat = get_list_or_404(Chat,pk=pk)
        serializer = ChatSerializer(chat,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)
    

class MessageCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request:Request):
        text = request.data.get("text")
        chat = request.data.get("chat")
        from_user = request.user.email
        serializer = MessageSerializer(data={"text":text,"chat":chat,'from_user':from_user})
        if serializer.is_valid():
            serializer.save()
            # BotV1(from_user).hello_user(chat_id = chat,text = text)
            
            return Response(data=serializer.data)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


