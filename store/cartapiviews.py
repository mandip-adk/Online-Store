from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import AddToCartSerializer, UpdateCartSerializer, RemoveCartSerializer
from .models import Product, Cart, CartProduct

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']

    # get product 
    
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

    # get or create cart
        cart, _ = Cart.objects.get_or_create(user=request.user)

    #get or create cart item
        cart_product , created = CartProduct.objects.get_or_create(
            cart=cart,
            product=product
    )

        if not created:
            cart_product.quantity += quantity
        else:
            cart_product.quantity = quantity

        cart_product.save()

        return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)

class UpdateCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UpdateCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']

    # get product 
    
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
    # get cart

        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({"error": "Cart not found"}, status=404)

    # get cart item
        try:
            cart_product = CartProduct.objects.get(cart=cart, product=product)
        except CartProduct.DoesNotExist:
            return Response({"error": "Item not in cart"}, status=404)
        
    # update quantity
        cart_product.quantity = quantity
        cart_product.save()

        return Response({"message": "Quantity updated"}, status=status.HTTP_200_OK)
    
class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RemoveCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']

    # get product
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

    # get cart
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({"error": "Cart not found"}, status=404)

    # delete item
        deleted, _ = CartProduct.objects.filter(cart=cart, product=product).delete()

        if deleted == 0:
            return Response({"error": "Item not in cart"}, status=404)

        return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
    
