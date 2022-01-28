from rest_framework import serializers
from bookstore.models.MusicStore import MusicStore

__all__ = ['MusicStoreSerializer']

class MusicStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = MusicStore
        fields = ('__all__')