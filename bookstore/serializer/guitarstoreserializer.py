from rest_framework import serializers
from bookstore.models.GuitarStore import GuitarStore

__all__ = ['GuitarStoreSerializer']

class GuitarStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = GuitarStore
        fields = ('__all__')