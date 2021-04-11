from django.urls import reverse
from toss.conftest import AuthAPITestCase


class TestUserAuth(AuthAPITestCase):

    def test_user_auth(self):
        res = self.client.get(reverse("user-me"))
        self.assertEqual(res.status_code, 200)
