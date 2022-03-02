from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from djoser.serializers import UserCreateSerializer
from . import models

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email')
        

