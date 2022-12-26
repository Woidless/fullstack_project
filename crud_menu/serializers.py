from rest_framework import serializers
from django.db.models import  Avg
from .models import DishMenu

class DishMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishMenu
        fields = ('__all__')