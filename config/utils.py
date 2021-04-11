from time import sleep


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
