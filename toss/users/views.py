import copy
import logging
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import models, serializers
from config.mixins import CustomResponseMixin
from .serializers import MyProfileSerializer, UserSerializer
from config.log import LOG
from .models import User

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet,
                  CustomResponseMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        """
             사용자 가입 SignUp API
         ---
         responseMessages:
             -   code:   200
                 message: SUCCESS
             -   code:   400
                 message: BADREQUEST
             -   code:   403
                 message: FORBIDDEN. (제재, 차단 사용자)
             -   code:   409
                 message: CONFLICT. (이미 가입된 사용자가 존재함)
             -   code:   500
                 message: SERVER ERROR
         """

        try:
            data_copy = copy.deepcopy(request.data)

            LOG(request=request, event='USER_NEW_SIGN',
                data=dict(extra=data_copy))

            signup_user = User.signup(data_copy)

            data = UserSerializer(signup_user).data

        except Exception as e:
            logger.error(e, exc_info=True)
            return self.server_exception()

        return self.success(results=data)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        """
            본인 Profile 조회 API
        ---
        response_serializer: users.serializers.MyProfileSerializer
        parameters:
            -   name: pk
                description : Profile 정보를 조회 할 User ID
                paramType: path
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

        serializer = MyProfileSerializer(
            request.user, context=dict(request=request)
        )

        return self.success(results=serializer.data)


    # TODO 내가 가진 컨트랙트 리스트