import re
from time import sleep
from enum import Enum
from django.utils import timezone


def send_email(email_to: str, html_body: str) -> bool:
    """
    지원자의 편의를 위해 테스트를 위한 더미 이메일 전송 함수를 구현해두었습니다.
    이메일 발송 로직을 구현하는 것 대신 이 함수를 사용해주세요.
    실제로 이메일이 발송되지는 않지만 잘 발송된다고 가정합니다.

    주의. 함수 내부 구현을 수정하지 말아주세요
    """
    sleep(180)
    print(email_to, html_body, flush=True)
    return True


def email_verification(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        print('Bad Syntax')
        raise ValueError('Bad Syntax')


def two_hour_hence():
    return timezone.now() + timezone.timedelta(days=2)


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def get_values(cls):
        return [x.value for x in cls]

    @classmethod
    def get_keys(cls):
        return [x.name for x in cls]
