from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer
from rest_framework import generics
# Create your views here.


#class MyBooksView(ModelViewSet):
#    queryset = models.MyBooks.objects.all()
#    serializer_class = serializer.MyBooksSerializer

class MyBooksViewAll(generics.ListCreateAPIView):
    queryset = models.MyBooks.objects.all()
    serializer_class = serializer.MyBooksSerializer
class MyBooksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MyBooks.objects.all()
    serializer_class = serializer.MyBooksSerializer