from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Person
from . import serializers
from .permissions import IsAuthor
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonListSerializer
    id_all_person = [i['owner_id'] for i in queryset.values()]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            if self.request.method == 'POST':
                print(self.id_all_person)
                print(self.request.user.id)
                if self.request.user.id in self.id_all_person:
                    # response.Response('У вас уже есть персонаж', status=400)
                    return [permissions.IsAdminUser()]
            return [permissions.IsAuthenticated(), IsAuthor()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    # def create(self, request, *args, **kwargs):
    #     print(request.data, '!!!!!!!!!!!!!!')
    #     Person.objects.create(
    #         age=request.data['age'],
    #         height=request.data['height'],
    #         weight=request.data['weight'],
    #         owner=request.user
    #     )
    #     return response.Response('ok', 201)