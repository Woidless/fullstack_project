from rest_framework import serializers
from django.db.models import Avg
from category.models import Category
from .models import Person


class PersonListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Person
        fields = ('__all__')


    def to_representation(self, instance):
        drs = super().to_representation(instance=instance)
        print(instance,
            '***'
        )
        drs['rating'] = instance.reviews.aggregate(Avg('rating'))['rating_avg']
        return drs



    