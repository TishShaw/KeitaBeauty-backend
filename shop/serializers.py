from rest_framework import serializers
from user.serializers import UserCreateSerializer
from .models import Product, Favorite, Review, Order, OrderItem, ShippingAddress, Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'shipping_address', 'phone_number')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'item', 'image',
                  'price', 'description', 'rating', 'numReviews', 'countInStock', 'is_active', 'reviews')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'owner')


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
