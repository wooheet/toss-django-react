import pytest

from toss.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    pass
