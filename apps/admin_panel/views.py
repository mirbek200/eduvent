from rest_framework import generics, permissions
from .models import CardCategories, Subcategories
from .serializers import CardCategoriesSerializer, SubcategoriesSerializer
from ..cards.models import Cards
from ..cards.serializers import CardSerializers


class CardCategoriesListView(generics.ListAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardCategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CardCategoriesCreateView(generics.CreateAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardCategoriesSerializer
    permission_classes = [permissions.IsAdminUser]


class CardCategoriesUpdateView(generics.UpdateAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardCategoriesSerializer
    permission_classes = [permissions.IsAdminUser]


class CardCategoriesDeleteView(generics.DestroyAPIView):
    queryset = CardCategories.objects.all()
    serializer_class = CardCategoriesSerializer
    permission_classes = [permissions.IsAdminUser]


class SubcategoriesListView(generics.ListAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubcategoriesCreateView(generics.CreateAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    permission_classes = [permissions.IsAdminUser]


class SubcategoriesUpdateView(generics.UpdateAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    permission_classes = [permissions.IsAdminUser]


class SubcategoriesDeleteView(generics.DestroyAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminCardDeleteView(generics.DestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers
    permission_classes = [permissions.IsAdminUser]













