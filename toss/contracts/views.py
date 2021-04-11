import copy
import logging
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .serializers import ContractSerializer
from config.mixins import CustomResponseMixin
from config.log import LOG
from .models import Contract

logger = logging.getLogger(__name__)


class ContractViewSet(viewsets.GenericViewSet,
                      CustomResponseMixin):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        """
            본인 Contract 조회 API
        ---
        response_serializer: users.serializers.ContractSerializer
        responseMessages:
            -   code:   200
                message: SUCCESS
            -   code:   404
                message: NOT FOUND
            -   code:   500
                message: SERVER ERROR
        """

        if not request.user.is_authenticated:
            return self.un_authorized()

        LOG(request=request, event='CONTRACT_LIST')

        cqs = Contract.objects.filter(
            contractor=request.user.id
        ).values_list('id', flat=True)

        serializer = ContractSerializer(cqs, many=True)

        return self.success(results=serializer.data)
