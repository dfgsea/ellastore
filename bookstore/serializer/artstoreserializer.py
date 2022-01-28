from rest_framework import serializers
from bookstore.models.ArtStore import ArtStore

__all__ = ['ArtStoreSerializer']

class ArtStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = ArtStore
        fields = ('__all__')