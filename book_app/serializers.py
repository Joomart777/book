from rest_framework import serializers

from book_app.models import Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

        fields = '__all__'