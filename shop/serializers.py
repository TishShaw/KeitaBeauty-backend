from rest_framework import serializers
from .models import Product, Favorite

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    product = serializers.HyperlinkedRelatedField(
        view_name='product_detail', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'item', 'image', 'price', 'description', 'is_active', 'product' )
        
# class OrderSerializer(serializers.HyperlinkedModelSerializer):

#     Order = serializers.HyperlinkedRelatedField(
#         view_name='order_detail', read_only=True)

#     class Meta:
#         model = Order
#         fields = ('id', 'customer_id', 'product', 'quantity','transacrtion_id', 'date_ordered', 'payment_type', 'is_complete')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    Favorite = serializers.HyperlinkedRelatedField(
        view_name='favorite_list', read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'products')
