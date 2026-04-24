from rest_framework import serializers
from .models import Category, Product, Cart, CartProduct, Order, OrderItem, Payment

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer (serializers.ModelSerializer):
    categories = CategorySerializer(many = True, read_only = True)
    class Meta:
        model = Product
        fields = '__all__'


class CartProductSerializer (serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    total_price = serializers.ReadOnlyField(source = 'get_total_price')
    class Meta:
        model = CartProduct
        fields = '__all__'


class CartSerializer (serializers.ModelSerializer):
    product = CartProductSerializer(many = True, read_only = True)
    class Meta:
        model = Cart
        fields = '__all__'

        
class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_total_price(self,obj):
        return obj.get_total_price()
    

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True, read_only = True)
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

        