from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer
# Create your views here.


class MyBooksView(ModelViewSet):
    queryset = models.MyBooks.objects.all()
    serializer_class = serializer.MyBooksSerializer