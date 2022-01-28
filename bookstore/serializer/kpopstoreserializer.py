from rest_framework import serializers
from bookstore.models.KpopStore import KpopStore

__all__ = ['KpopStoreSerializer']

class KpopStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = KpopStore
        fields = ('__all__')