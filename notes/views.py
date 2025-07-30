from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import node
from .serializers import nodeSerializer
from django.shortcuts import get_object_or_404


class nodeListCreate(APIView):
    def get(self,request:Request):
        nodes = node.objects.all()
        serializer = nodeSerializer(nodes,many=True)
        return Response(serializer.data)
    def post(self,request:Request):
        serializer = nodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class nodeDetailView(APIView):
    def get(self,request:Request,pk):
        obj = get_object_or_404(node,pk=pk)
        serializer = nodeSerializer(obj)
        return Response(serializer.data)
    def delete(self,request:Request,pk):
        obj = get_object_or_404(node,pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request:Request,pk):
        obj = get_object_or_404(node,pk=pk)
        serializer = nodeSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request:Request,pk):
        obj = get_object_or_404(node,pk=pk)
        serializer = nodeSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class nodeUpgradeView(APIView):
    def post(self,request:Request,pk):
        obj = get_object_or_404(node,pk=pk)
        obj.content = obj.content.upper()
        obj.title = obj.title.upper()
        obj.save()
        serializer = nodeSerializer(obj)
        return Response(data=serializer.data)
class nodeLowerView(APIView):
    def post(self,request:Request,pk):
        obj = get_object_or_404(node,pk=pk)
        obj.title = obj.title.lower()
        obj.content = obj.content.lower()
        obj.save()
        serializer = nodeSerializer(obj)
        return Response(data=serializer.data)