from rest_framework import generics, permissions
from .models import CardCategories
from .serializers import CardSerializer


class CardCategoriesListView(generics.ListAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardSerializer


class CardCategoriesCreateView(generics.CreateAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAdminUser]


class CardCategoriesUpdateView(generics.UpdateAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAdminUser]


class CardCategoriesDeleteView(generics.DestroyAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAdminUser]
