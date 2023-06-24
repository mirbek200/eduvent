from django.http import Http404
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, generics, permissions, exceptions
from rest_framework.response import Response

from .models import MyUser, Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, LoginSerializer, ProfileSerializer, ProfileListSerializer


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
            # user.create_activation_code()
            # user.send_activation_code()
            user.save()
            profile = Profile.objects.create(
                user=user
            )
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ActivationView(APIView):
#     def get(self, request, activation_code):
#         try:
#             user = MyUser.objects.get(activation_code=activation_code)
#             user.is_active = True
#             user.activation_code = ''
#             user.save()
#             return Response('Вы успешно активировали аккаунт')
#         except MyUser.DoesNotExist:
#             raise Http404


class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]


class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


