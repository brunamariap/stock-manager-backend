from .models import Product, ProductSold
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'url','name', 'amount', 'unitary_value', 'created_at', 'updated_at']


class ProductSoldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductSold
        fields = ['id','url', 'product', 'sold_amount', 'final_value', 'created_at']   