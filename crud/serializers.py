from rest_framework import serializers
from django.db.models import Avg
from .models import Person


class PersonListSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='person.owner.username')

    class Meta:
        model = Person
        fields = ('owner', 'age', 'height', 'weight',
                    'sex', 'blood_type', 'allergy', 
                    'symptoms', 'disability',
                    'injury', 'illness', 'person_images')

    # def to_representation(self, instance):
    #     drs = super().to_representation(instance=instance)
    #     drs['rating'] = instance.reviews.aggregate(Avg('rating'))['rating_avg']
    #     return drs


# class PersonSettingsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         exclude = ('owner',)

#     def save(self, **kwargs):
#         data = self.validated_data
#         user = data.user
#         user.save()
#         return user

    