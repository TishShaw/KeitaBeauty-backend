from rest_framework import serializers
from .models import Product, Favorite, Review, Order, CartItem, ShippingAddress


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'owner', 'product_id', 'review_title', 'review_body', )


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'item', 'image', 'price', 'description',
                  'reviews', 'is_active', 'category_name')

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
    owner = serializers.ReadOnlyField(source='owner.username')
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    class Meta:
        model = Favorite
        fields = ('id', 'products', 'product_id', 'name', 'owner')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='product_detail', read_only=True)

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    class Meta:
        model = CartItem
        fields = ('id', 'name', 'product', 'quantity', 'product_id')
