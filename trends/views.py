from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Trend,TrendNews
from .serializers import TrendSerializer,TrendNewsSerializer

from .botV2 import BotV2

from django.shortcuts import get_object_or_404

class TrendListCreate(APIView):
    def get(self,request:Request):
        trends = Trend.objects.all()
        serializer = TrendSerializer(trends,many=True)
        return Response(serializer.data)
    def post(self,request:Request):
        serializer = TrendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TrendDetailView(APIView):
    def get(self,request:Request,pk):
        trend = get_object_or_404(Trend,pk=pk)
        serializer = TrendSerializer(trend)
        return Response(serializer.data)
    def patch(self,request,pk):
        trend = get_object_or_404(Trend,pk=pk)
        serializer = TrendSerializer(trend,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request:Request,pk):
        trend = get_object_or_404(Trend,pk=pk)
        trend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,data="Deleted")

class TrendNewsListViews(APIView):
    def get(self,request:Request):
        trend_news = TrendNews.objects.all()
        serializer = TrendNewsSerializer(trend_news,many=True)
        return Response(serializer.data)

class BotCommandSys(APIView):
    def post(self,request:Request):
        command = request.data.get("command")
        res = BotV2().Command(command)
        return Response(res)
        
        