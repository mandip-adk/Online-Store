from rest_framework import viewsets
from .models import (
    Category, Product, 
    CartProduct, Cart,
    Payment , OrderItem, Order)
from .serializers import (
    CategorySerializer, ProductSerializer, 
    CartProductSerializer, CartSerializer, 
    OrderItemSerializer, OrderSerializer)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

