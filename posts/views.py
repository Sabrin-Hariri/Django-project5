from django.shortcuts import render
from rest_framework.parsers import JSONParser 
from rest_framework import viewsets
from .serializers import POSTSerializer
from .models import Post


class PostView(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = POSTSerializer