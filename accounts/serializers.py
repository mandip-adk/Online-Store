from rest_framework import serializers
from .models import CustomUser, DeliveryPerson, ShippingAddress

# User serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email','password', 'role', 'is_active']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email= validated_data['email'],
            password= validated_data['password'],
            role = validated_data.get('role', 'customer')
        )
        return user

# Shipping Address serializer
class ShippingAddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    
    class Meta:
        model = ShippingAddress
        fields = '__all__'

# Delivery Person Serializer
class DeliveryPersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = DeliveryPerson
        fields = '__all__'

