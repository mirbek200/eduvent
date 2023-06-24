# from django.conf import settings
#
#
# def send_activation_mail(email, activation_code):
#     from django.core.mail import send_mail
#     activation_link = f'http://127.0.0.1:9000/api/users/activation/{activation_code}'
#     send_mail(
#         'Account activation',
#         message=activation_link,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[email],
#         fail_silently=False)
