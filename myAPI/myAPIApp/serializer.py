from rest_framework import serializers
from . import models
from decimal import Decimal
class MyBooksSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source="inventory")
    calculated_price = serializers.SerializerMethodField(method_name='calculate_tax')
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    class Meta:
        
        model = models.MyBooks
        fields =['id', 'title', 'price', 'stock', 'calculated_price', 'category']
    def calculate_tax(self, product: models.MyBooks):
        new_price = product.price + product.price*Decimal(0.5)
        return (new_price)
