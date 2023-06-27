from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class CustomUserManager(BaseUserManager):

    def _create(self, email, password, name, phone_number, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, name, phone_number, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, name, phone_number, **extra_fields)

    def create_superuser(self, email, password, name, phone_number, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create(email, password, name, phone_number, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    # activation_code = models.CharField(max_length=20, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    # def create_activation_code(self):
    #     from django.utils.crypto import get_random_string
    #     code = get_random_string(20)
    #     self.activation_code = code
    #     self.save()
    #     return code

    # def send_activation_code(self):
    #     from django.core.mail import send_mail
    #     activation_link = f'http://127.0.0.1:9000/api/users/activation/{self.activation_code}'
    #     send_mail(
    #         'Account activation',
    #         message=activation_link,
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[self.email],
    #         fail_silently=False)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_avatar = models.ImageField(upload_to='media/avatars/', null=False, blank=False)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_description = models.CharField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.is_company = True
        self.user.save()

