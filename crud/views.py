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
    # id_all_person = [i['owner_id'] for i in queryset.values()]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            if self.request.method == 'POST':
                try:    
                    if User.person_status:
                        return [permissions.IsAdminUser()]
                except:
                    print(self.request.user.person_status, '!!!!!!!!'*50)
                    User.person_status = True
                    return [permissions.IsAuthenticated(), IsAuthor()]         
            print(self.request.user.person_status, '!!!!!!!!'*50)
            User.person_status = True
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