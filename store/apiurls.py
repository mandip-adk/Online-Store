from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import CategoryViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet)


urlpatterns = [
    path ('', include(router.urls)),
]