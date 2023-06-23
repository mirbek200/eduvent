from django.http import Http404
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response

from .models import MyUser, Profile
from .serializers import UserSerializer, LoginSerializer, ProfileSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegistrationAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = MyUser.objects.create_user(
                name=request.data['name'],
                email=request.data['email'],
                phone_number=request.data['phone_number'],
                password=request.data['password'],
            )
            user.create_activation_code()
            user.send_activation_code()
            user.save()
            profile = Profile.objects.create(
                user=user
            )
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = MyUser.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Вы успешно активировали аккаунт')
        except MyUser.DoesNotExist:
            raise Http404


class ProfileUpdateAPIView(APIView):
    serializer_class = ProfileSerializer
    # permission_classes = [IsAdminUser]

    def get_object(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        profile = self.get_object(id)
        serializer = ProfileSerializer(profile, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailApiView(APIView):

    def get_object(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, id):
        profile = self.get_object(id)
        serializers = ProfileSerializer(profile)
        data = serializers.data
        return Response(data)

