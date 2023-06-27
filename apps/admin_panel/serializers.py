from rest_framework import serializers
from .models import CardCategories


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardCategories
        fields = "__all__"
