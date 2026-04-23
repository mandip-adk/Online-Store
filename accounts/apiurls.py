from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import UserViewSet, DeliveryViewSet, ShippingViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('delivery', DeliveryViewSet)
router.register('address', ShippingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]