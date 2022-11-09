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

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsAuthor()]

    # @action(['DELETE'], detail=True)
    # def delete_person(self, request, pk):
    #     if request.method == 'DELETE':
    #         if User.person_status:
    #             if self.user == User.owner:
    #                 User.person_status = False
    #                 return response.Response('Deleted', status=204)
    #         return response.Response('Персонажа нет', status=400)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save(status=self.request.user.email)
    
    # def create(self, request, *args, **kwargs):
    #     print(request.data, '!!!!!!!!!!!!!!')
    #     Person.objects.create(
    #         age=request.data['age'],
    #         height=request.data['height'],
    #         weight=request.data['weight'],
    #         owner=request.user
    #     )
    #     return response.Response('ok', 201)