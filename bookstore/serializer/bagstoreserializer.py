from rest_framework import serializers
from bookstore.models.BagStore import BagStore

__all__ = ['BagStoreSerializer']

class BagStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = BagStore
        fields = ('__all__')