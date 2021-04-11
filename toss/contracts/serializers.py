from rest_framework import serializers
from rest_framework.serializers import ListSerializer
from . import models


class ContractIdListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()


class ContractListSerializer(ListSerializer):

    def to_representation(self, profile_list):
        serialized_profile_list = ContractIdListSerializer(profile_list, many=True).data

        return serialized_profile_list


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = ContractListSerializer


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contract
        fields = '__all__'