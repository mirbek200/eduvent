from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .tasks import send_activation_mail
from .models import MyUser, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'name', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self):
            user = MyUser.objects.create_user(**self.validated_data)
            user.create_activation_code()
            send_activation_mail.delay(user.email, user.activation_code)
            return user


class LoginSerializer(serializers.Serializer):
    email_or_phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = None
        if '@' in data['email_or_phone_number']:
            user = MyUser.objects.filter(email=data['email_or_phone_number']).first()
        else:
            user = MyUser.objects.filter(phone_number=data['email_or_phone_number']).first()

        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return {
                'email': user.email,
                'phone_number': user.phone_number,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        raise serializers.ValidationError('Incorrect email/phone number or password')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['company_avatar', 'company_name', 'company_description']
