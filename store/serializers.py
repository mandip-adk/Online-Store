from rest_framework import serializers
from .models import Category, Product, Cart, CartProduct, Order, OrderItem, Payment

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BaseProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        source='categories'
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'image',
            'description', 'created_at', 'updated_at',
            'categories', 'category_ids'
        ]


class ProductPublicSerializer(BaseProductSerializer):
    pass


class ProductAdminSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = BaseProductSerializer.Meta.fields + ['featured']

class CartProductSerializer (serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    total_price = serializers.ReadOnlyField(source = 'get_total_price')
    class Meta:
        model = CartProduct
        fields = '__all__'


class CartSerializer (serializers.ModelSerializer):
    products = CartProductSerializer(many = True, read_only = True)
    total_cart_price = serializers.SerializerMethodField()

    def get_total_cart_price(self,obj):
        return sum (
            item.quantity * item.product.price
            for item in obj.products.all()
        )
    
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


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default = 1)


class UpdateCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class RemoveCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

        