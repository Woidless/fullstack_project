from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from .models import DishMenu
from . import serializers
from .permissions import IsAuthor


class DishMenuViewSet(ModelViewSet):
    queryset = DishMenu.objects.all()
    serializer_class = serializers.DishMenuSerializer


    def get_permissions(self):
        if self.request.method == 'GET': return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save(owner=self.request.user.email)