from django.utils import timezone
from config.utils import ChoiceEnum, two_hour_hence
from django.db import models, transaction, IntegrityError
from django.core.exceptions import ValidationError
from config.utils import send_email


class Contract(models.Model):
    class Article(ChoiceEnum):
        FIRST = '이용허락'

    contractor = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='contractor'
    )
    start_term = models.DateTimeField(default=timezone.now)
    end_term = models.DateTimeField(default=two_hour_hence)
    term_of_contract = models.CharField(choices=Article.choices(), max_length=300,
                                        blank=True, null=True)
    associate_contract = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    @classmethod
    def create(cls, user):
        try:
            with transaction.atomic():
                contract = cls.objects.create(
                    contractor=user, term_of_contract=str(Contract.Article.FIRST),
                    start_term=timezone.now(), end_term=two_hour_hence()
                )
        except ValidationError:
            raise ValidationError('User data is invalid.')
        except IntegrityError:
            # TODO 중복 체크
            pass

        # send_email(user.email, 'body')

        return contract
