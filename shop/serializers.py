from rest_framework import serializers
from user.serializers import UserCreateSerializer
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
                  'reviews', 'is_active', 'category_name', 'countInStock')


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
        fields = ('id','product', 'products', 'product_id', 'name', 'owner')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='product_detail', read_only=True)

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    class Meta:
        model = CartItem
        fields = '__all__'


class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    Order = serializers.HyperlinkedRelatedField(
        view_name='order_detail', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_cartItem(self, obj):
        items = obj.cartItem_set.all()
        serializer = CartItemSerializer(items, many=True)
        return serializer.data

    
    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(
                obj.shippingaddress, many=False).data
        except:
            address = False
        return address

    def get_user(self, obj):
        user = obj.user
        serializer = UserCreateSerializer(user, many=False)
        return serializer.data