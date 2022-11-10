from rest_framework import serializers
from django.db.models import Avg
from .models import Person


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('__all__')