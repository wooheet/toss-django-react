from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
        )


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
        fields = (
            'id',
            'username',
            'name'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields ='__all__'
