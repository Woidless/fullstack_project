from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.ShopViewSet, basename='shop')


urlpatterns = [
    path('', include(router.urls)),
]