from .models import Shop
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ShopSerializers(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ('title', 'photo', 'description', 'price',)