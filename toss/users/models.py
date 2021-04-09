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

    profile_image = models.ImageField(null=True)
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    @property
    def post_count(self):
        return self.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()

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
