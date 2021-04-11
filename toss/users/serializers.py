from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('username')


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'name'
        )


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields ='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields ='__all__'
