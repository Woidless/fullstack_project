from .models import Shop
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg

User = get_user_model()


class ShopSerializers(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ('title', 'photo', 'description', 'price',)

    def to_representation(self, instance):
        repr =  super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr