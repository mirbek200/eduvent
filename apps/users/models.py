from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, email, phone_number, password=None, name=None, is_company=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            name=name,
            is_company=is_company
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=20, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(20)
        self.activation_code = code
        self.save()
        return code

    def send_activation_code(self):
        from django.core.mail import send_mail
        activation_link = f'http://127.0.0.1:9000/api/users/activation/{self.activation_code}'
        send_mail(
            'Account activation',
            message=activation_link,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.email],
            fail_silently=False)


class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatars/', null=False, blank=False)
    name_of_company = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)














