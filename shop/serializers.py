from rest_framework import serializers
from user.serializers import UserCreateSerializer
from .models import Product, Favorite, Review, Order, OrderItem, ShippingAddress


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'review_title', 'review_body', 'product', 'owner', 'product_id')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'item', 'image', 'price', 'description', 'is_active', 'reviews')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        view_name='product_detail', read_only=True, many=True)

    name = serializers.ReadOnlyField(source='product.item')
    owner = serializers.ReadOnlyField(source='owner.username')
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'owner', 'products', 'name', 'product_id')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
