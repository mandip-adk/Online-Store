from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import CategoryViewSet, ProductViewSet, CartViewSet
from .cartapiviews import AddToCartView, UpdateCartView, RemoveFromCartView

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('cart',CartViewSet)


urlpatterns = [
    path ('', include(router.urls)),

    #path for apiview
    path('add-to-cart/', AddToCartView.as_view(), name = 'add-to-cart'),
    path('update-cart/', UpdateCartView.as_view()),
    path('remove-from-cart/', RemoveFromCartView.as_view()),
    
]