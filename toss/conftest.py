import pytest

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from toss.users.models import User
from toss.users.tests.factories import UserFactory


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
        username = kwargs.get("username", "name")
        password = kwargs.get("password", "password")
        email = kwargs.get("email", "teddy@toss.io")

        client = APIClient()
        client.credentials(HTTP_USER_AGENT="AuthServer")

        signup_data = {
            username: username,
            password: password,
            email: email
        }

        res = client.post(reverse("users-list"),
                          signup_data, format="json")

        # client.credentials(HTTP_AUTHORIZATION="JWT %s" % self.jwt_token)

        # client_data = res.data.get("results")[0]
        #
        # self.user_id = client_data.get("id")
        #
        # return client_data, client

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
