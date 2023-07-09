from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, generics, permissions, serializers
from rest_framework.response import Response

from .models import MyUser, Profile
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, LoginSerializer, ProfileSerializer, ProfileListSerializer
from ..cards.models import Cards
from ..cards.serializers import CardSerializers
from ..review.models import Review
from ..review.serializers import ReviewSerializer


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

            profile = Profile.objects.create(user=user)
            profile.save()
            access_token = generate_access_token(user)

            response_data = {
                'access_token': access_token,
                'user': serializer.data,
                'user_id': user.id
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=3)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


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
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update_user_is_company(self, user):
        user.is_company = True
        user.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        user = get_object_or_404(MyUser, pk=instance.user.pk)
        self.update_user_is_company(user)


class ProfileCardListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, user_id):
        try:
            user = MyUser.objects.get(id=user_id)
            cards = Cards.objects.filter(user=user)

            card_serializer = CardSerializers(cards, many=True)

            data = {
                'cards': card_serializer.data
            }

            return Response(data)
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ProfileDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, user_id):
        try:
            user = MyUser.objects.get(id=user_id)
            profile = Profile.objects.filter(user=user)
            review = Review.objects.filter(user=user)

            review_serializer = ReviewSerializer(review, many=True)
            profile_serializer = ProfileSerializer(profile, many=True)

            data = {
                'profile': profile_serializer.data,
                'review': review_serializer.data
            }

            return Response(data)
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
