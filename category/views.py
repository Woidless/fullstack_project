from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Category
from . import serializers


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]