import pytest

from rest_framework.test import APIClient, APITestCase
from toss.users.models import User
from toss.users.tests.factories import UserFactory
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


class AuthAPITestCase(APITestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def signup_user(self, **kwargs):
        client = APIClient()
        client.credentials(HTTP_USER_AGENT="AuthServer")

        user_factory = UserFactory()

        payload = jwt_payload_handler(user_factory)
        token = jwt_encode_handler(payload)

        client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))

        return client

    def setUp(self, **kwargs):
        super().setUp()
        self.signup_user(**kwargs)
        # self.user, self.client = self.signup_user(**kwargs)
        # self.no_signup_client = APIClient()

    def many_signup(self, count):
        signup_list = list(
            map(
                lambda x: self.signup_user(nickname=f"user{x}"), range(0, count)
            )
        )
        user_list = []
        client_list = []
        for u, c in signup_list:
            user_list.append(u)
            client_list.append(c)
        return user_list, client_list

    def get_user(self):
        return User.objects.get(id=self.user["id"])

    def get_user_object(self):
        return User.objects.get(id=self.user_id)
