import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from django.urls import reverse

from toss.users.forms import UserChangeForm
from toss.users.models import User
from toss.users.tests.factories import UserFactory
from toss.users.views import (
    UserProfile
)

pytestmark = pytest.mark.django_db


