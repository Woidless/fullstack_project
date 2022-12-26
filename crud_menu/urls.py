from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.DishMenuViewSet, basename='dish_menu')

urlpatterns = [
    path('addDish', include(router.urls))
]