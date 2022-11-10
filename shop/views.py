from rest_framework import response, permissions
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .models import Shop
from rest_framework.response import Response
from .serializers import ShopSerializers
from . import serializers
from .permissions import IsAuthor


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsAuthor()]
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
