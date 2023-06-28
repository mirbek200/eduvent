from .models import Cards
from rest_framework import generics
from .serializers import CardSerializers
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsOwnerOrReadOnly


class CardCreateView(generics.CreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers
    permission_classes = [IsAuthenticated]


class CardListView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers
    permission_classes = [IsAuthenticated]


class CardUpdateView(generics.UpdateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class CardDeleteView(generics.DestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]