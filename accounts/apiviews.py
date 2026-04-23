from rest_framework import viewsets
from .models import CustomUser, DeliveryPerson, ShippingAddress
from .serializers import(
    UserSerializer,
    DeliveryPersonSerializer,
    ShippingAddressSerializer
)
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer

    def get_queryset(self):
        return DeliveryPerson.objects.filter(user=self.request.user)

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

