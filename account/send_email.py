from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://l34.28.220.66/accounts/activate/{code}/'
    send_mail(
        'Hello! Activate your account!',
        f'To activate your account you need to link: {full_link}',
        'abdb2226@gmail.com',
        [user],
        fail_silently=False
    )


