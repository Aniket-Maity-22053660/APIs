from rest_framework import serializers
from . import models
class MyBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyBooks
        fields = "__all__"