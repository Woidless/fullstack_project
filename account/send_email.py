from django.core.mail import send_mail

def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/accounts/activate/{code}/'
    send_mail(
        'Hello! Activate your account!!!'
        f'{"Mr." if user.sex=="male" else "Ms."}{user.name} {user.surname}, to activate your account you need to link: {full_link}'
        'abdb2226@gmail.com',
        [user],
        fail_silently=False
    )


