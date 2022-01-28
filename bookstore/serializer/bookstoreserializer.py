from rest_framework import serializers
from bookstore.models.BookStore import BookStore

__all__ = ['BookStoreSerializer']

class BookStoreSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    class Meta:
        model = BookStore
        fields = ('__all__')