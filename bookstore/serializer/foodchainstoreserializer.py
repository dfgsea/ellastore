from rest_framework import serializers
from bookstore.models.FoodchainStore import FoodchainStore

__all__ = ['FoodchainStoreSerializer']

class FoodchainStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = FoodchainStore
        fields = ('__all__')