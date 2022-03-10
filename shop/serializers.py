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
        fields = ('id', 'review_title', 'review_body',
                  'product', 'owner', 'product_id', 'rating')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    countInStock = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'category_name', 'item', 'image',
                  'price', 'description', 'countInStock', 'is_active', 'reviews')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'owner')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'name', 'product', 'order', 'image', 'qty', 'price')


class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ('id', 'order', 'customer_address', 'customer_city',
                  'customer_postalCode', 'country', 'shipping_fee')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'date_ordered', 'total_price', 'shipping_price', 'payment_type',
                  'is_paid', 'paidAt', 'is_delivered', 'deliveredAt', 'created_at', 'orderItem', 'shippingAddress', 'user')
