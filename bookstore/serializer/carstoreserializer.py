from rest_framework import serializers
from bookstore.models.CarStore import CarStore

__all__ = ['CarStoreSerializer']

class CarStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = CarStore
        fields = ('__all__')