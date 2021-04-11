import copy
import logging
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from toss.users.models import User
from config.log import LOG
from .models import Contract
from config.mixins import CustomResponseMixin
from .serializers import ContractSerializer, ContractCreateSerializer

logger = logging.getLogger(__name__)


class ContractViewSet(viewsets.GenericViewSet,
                      CustomResponseMixin):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        """
            Create contract
         ---
         responseMessages:
             -   code:   200
                 message: SUCCESS
             -   code:   400
                 message: BADREQUEST
             -   code:   403
                 message: FORBIDDEN.
             -   code:   500
                 message: SERVER ERROR
         """

        try:
            data_copy = copy.deepcopy(request.data)

            LOG(request=request, event='CREATE_CONTRACT',
                data=dict(extra=data_copy))

            user = User.signup(data_copy)
            contract = Contract.create(user)

            data = ContractCreateSerializer(contract).data

        except Exception as e:
            logger.error(e, exc_info=True)
            return self.server_exception()

        return self.success(results=data)

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
