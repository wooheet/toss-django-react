from django.urls import reverse
from toss.conftest import AuthAPITestCase
from .models import Contract
from toss.users.models import User
from django.utils import timezone
from config.utils import two_hour_hence


class TestContract(AuthAPITestCase):

    def test_get_my_contract_list(self):
        user = User.objects.get(pk=self.user_id)

        for i in range(2):
            Contract.objects.create(
                contractor=user, term_of_contract=Contract.Article.FIRST,
                start_term=timezone.now(), end_term=two_hour_hence()
            )

        res = self.client.get(reverse("contract-list"))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get('results')), 2)

    def test_create_contract(self):
        res = self.client.post(reverse("contract-list"))
        self.assertEqual(res.status_code, 200)
