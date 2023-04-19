from .models import Product, ProductSold
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'amount', 'unitary_value', 'created_at', 'updated_at']


class ProductSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSold
        fields = ['id', 'product_id', 'sold_amount', 'final_value', 'created_at']   