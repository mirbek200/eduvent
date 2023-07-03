from rest_framework import serializers
from .models import CardCategories, Subcategories


class CardCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardCategories
        fields = "__all__"


class SubcategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategories
        fields = '__all__'
