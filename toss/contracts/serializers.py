from rest_framework import serializers
from . import models


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract
        fields = (
            'id',
        )

