from django.db.models import fields
from rest_framework import serializers
from products.models import Categories, Product

# class ProductSerializer(serializers.Serializer):
#     name        = serializers.CharField(max_length=225)
#     description = serializers.CharField()
#     price       = serializers.DecimalField(max_digits=6, decimal_places=2)
#     sold        = serializers.BooleanField()
#     soldon      = serializers.DateTimeField()
#     featured    = serializers.BooleanField()

#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.sold = validated_data.get('sold', instance.sold)
#         instance.soldon = validated_data.get('soldon', instance.soldon)
#         instance.featured = validated_data.get('featured', instance.featured)
#         instance.save()
#         return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'