from rest_framework import viewsets
from .models import (
    Category, Product, 
    CartProduct, Cart,
    Payment , OrderItem, Order)
from .serializers import (
    CategorySerializer, ProductPublicSerializer,
    ProductAdminSerializer, BaseProductSerializer,
    CartProductSerializer, CartSerializer, 
    OrderItemSerializer, OrderSerializer)
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('categories')
    serializer_class = ProductPublicSerializer  # fallback

    def get_serializer_class(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return ProductAdminSerializer
        return ProductPublicSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    

