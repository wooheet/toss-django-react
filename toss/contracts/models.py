from django.db import models
from django.utils import timezone
from config.utils import ChoiceEnum


class Contract(models.Model):
    class Article(ChoiceEnum):
        FIRST = '이용허락'


    contractor = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='contractor'
    )
    term = models.DateTimeField()
    term_of_contract = models.CharField(choices=Article.choices(), max_length=300,
                                        blank=True, null=True)
    associate_contract = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
