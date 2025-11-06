from rest_framework import serializers
from ..models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id','name']
        
        
# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#     class Meta:
#         model = Product
#         fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    # Allow category assignment via ID
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'category_id']
