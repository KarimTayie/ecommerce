from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product, Order, OrderItem, ShippingAddress, Review


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id")
    name = serializers.SerializerMethodField()
    isAdmin = serializers.BooleanField(source="is_staff")

    class Meta:
        model = User
        fields = ["_id", "username", "email", "name", "isAdmin"]

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["_id", "username", "email", "name", "isAdmin", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, source="review_set")

    class Meta:
        model = Product
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    orderItems = OrderItemSerializer(many=True, source="orderitem_set")
    shippingAddress = ShippingAddressSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = "__all__"
