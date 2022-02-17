from rest_framework import serializers
from .models import Product, Favorite

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'item', 'image', 'price', 'description',
                'is_active')
        
# class OrderSerializer(serializers.HyperlinkedModelSerializer):

#     Order = serializers.HyperlinkedRelatedField(
#         view_name='order_detail', read_only=True)

#     class Meta:
#         model = Order
#         fields = ('id', 'customer_id', 'product', 'quantity','transacrtion_id', 'date_ordered', 'payment_type', 'is_complete')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        view_name='product_detail', read_only=True)
    
    name = serializers.ReadOnlyField(source='product.item')
    owner =serializers.ReadOnlyField(source='owner.username')
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )
    
    class Meta:
        model = Favorite
        fields = ('id', 'products', 'product_id', 'name', 'owner')
