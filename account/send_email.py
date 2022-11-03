from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://34.28.220.66/accounts/activate/{code}/'
    send_mail(
        'Hello! Activate your account!',
        f'To activate your account you need to link: {full_link}',
        'abdb2226@gmail.com',
        [user],
        fail_silently=False
    )


def send_code_password_reset(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'Code for restore',
        f'Your code: {code}',
        'abdb2226@gmail.com',
        [email],
        fail_silently=False
    )