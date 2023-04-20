from .models import Product, ProductSold
from django.shortcuts import render
from .serializers import ProductSerializer, ProductSoldSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSoldViewSet(viewsets.ModelViewSet):
    queryset = ProductSold.objects.all()
    serializer_class = ProductSoldSerializer