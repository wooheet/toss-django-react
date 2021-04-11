from rest_framework import serializers
from rest_framework.serializers import ListSerializer


class ContractIdListSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ContractListSerializer(ListSerializer):

    def to_representation(self, profile_list):
        serialized_profile_list = ContractIdListSerializer(profile_list, many=True).data

        return serialized_profile_list


class ContractSerializer(serializers.Serializer):

    class Meta:
        list_serializer_class = ContractListSerializer