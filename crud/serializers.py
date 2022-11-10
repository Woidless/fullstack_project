from rest_framework import serializers
from django.db.models import Avg
from .models import Person


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id','owner', 'age', 'name', 'surname',
                    'height', 'weight','sex', 'blood_type',
                    'allergy', 'symptoms', 'disability',
                    'injury', 'illness', 'person_images',)