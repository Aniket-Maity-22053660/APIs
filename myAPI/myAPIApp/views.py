from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.


#class MyBooksView(ModelViewSet):
#    queryset = models.MyBooks.objects.all()
#    serializer_class = serializer.MyBooksSerializer

'''
class MyBooksViewAll(generics.ListCreateAPIView):
    queryset = models.MyBooks.objects.all()
    serializer_class = serializer.MyBooksSerializer
class MyBooksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MyBooks.objects.all()
    serializer_class = serializer.MyBooksSerializer
'''

class MyBooksView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        items = models.MyBooks.objects.all()
        inventory = request.query_params.get('stock')
        category = request.query_params.get('category')
        price_gt = request.query_params.get('price_gt')
        price_lt = request.query_params.get('price_lt')
        contains = request.query_params.get('contains')
        starts_with = request.query_params.get('starts_with')
        ordering = request.query_params.get('order')
        if inventory:
            items = items.filter(inventory=inventory)
        if category:
            items = items.filter(category= category)
        if price_gt:
            items = items.filter(price__gte = price_gt)
        if price_lt:
            items = items.filter(price__lte = price_lt)
        if contains:
            items = items.filter(title__icontains = contains)
        if starts_with:
            items = items.filter(title__istartswith = starts_with)
        if ordering:
            items = items.order_by(ordering)
        
        serialized_item = serializer.MyBooksSerializer(items, many=True)
        return Response(serialized_item.data)
    def create(self, request):
        serialized_item = serializer.MyBooksSerializer(data= request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        else:
            return Response(serialized_item.errors)
    def retrieve(self, request, pk = None):
        item = models.MyBooks.objects.filter(pk=pk).first()
        if not item:
            return Response({'message':'Data not found'})
        serialized_item = serializer.MyBooksSerializer(item)
        return Response(serialized_item.data)
    def update(self, request, pk=None):
        item = models.MyBooks.objects.filter(pk=pk).first()
        if not item:
            return Response({'message': 'Data not found'})
        serialized_item = serializer.MyBooksSerializer(item, data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        return Response(serialized_item.errors)
    def partial_update(self, request, pk=None):
        item = models.MyBooks.objects.filter(pk=pk).first()
        if not item:
            return Response({'message' : 'Data not found'})
        serialized_item = serializer.MyBooksSerializer(item, data=request.data, partial=True)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        return Response(serialized_items.errors)
    def destroy(self, request, pk=None):
        item = models.MyBooks.objects.filter(pk=pk).first()
        if not item:
            return Response({'message' : 'Data not found'})
        item.delete()
        return Response({'message' : 'item deleted successfully'})


        