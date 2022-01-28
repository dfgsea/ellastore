from rest_framework import serializers
from bookstore.models.ClothingStore import ClothingStore

__all__ = ['ClothingStoreSerializer']

class ClothingStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = ClothingStore
        fields = ('__all__')