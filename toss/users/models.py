from django.contrib.auth.models import AbstractUser
from django.db import models, transaction, IntegrityError
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Toss."""

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    @classmethod
    def signup(cls, params):
        email = params.get('email', '')
        username = params.get('username', '')

        try:
            with transaction.atomic():
                signup_user = cls.objects.create(
                    username=username, email=email
                )
        except ValidationError:
            raise ValidationError('User data is invalid.')
        except IntegrityError:
            signup_user = cls.objects.get(username=username)

        return signup_user
