from django.conf import settings
from django.urls import path, include
from . import views
urlpatterns = [
    path('product/', views.ProductViewSet.as_view())
]