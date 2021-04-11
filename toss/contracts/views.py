import logging
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist

from config.log import LOG
from .models import Contract
from config.mixins import CustomResponseMixin, CustomPaginatorMixin
from .serializers import ContractSerializer

logger = logging.getLogger(__name__)


class ContractViewSet(viewsets.GenericViewSet,
                      CustomResponseMixin,
                      CustomPaginatorMixin):
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

        try:
            cqs = Contract.objects.filter(
                contractor=request.user.id)

            serializer = ContractSerializer(cqs, many=True)

            return self.success(results=serializer.data)
        except ObjectDoesNotExist:
            return self.not_found()
