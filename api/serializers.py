from rest_framework import serializers
from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Product
        fields = [
            'url',
            'pk',
            'title',
            'description',
            'category',
            'created',
        ]



class ProductsSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
