from rest_framework import serializers
from ParfumeCosmetic.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'description', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'category', 'category_id', 'name', 'slug', 'image', 
                  'description', 'price', 'old_price', 'is_available', 
                  'is_featured', 'is_new', 'created_at', 'updated_at']