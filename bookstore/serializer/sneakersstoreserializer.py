from rest_framework import serializers
from bookstore.models.SneakersStore import SneakersStore

__all__ = ['SneakersStoreSerializer']

class SneakersStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = SneakersStore
        fields = ('__all__')