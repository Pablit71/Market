from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import User


# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'