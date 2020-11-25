from rest_framework import serializers
from orders.models import OrderInfo, OrderGoods
from goods.models import SKU


class OrdersSerializer(serializers.ModelSerializer):
    """
        订单序列化器
    """

    class Meta:
        model = OrderInfo
        fields = ('order_id', 'create_time')


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ('name', 'default_image')


class OrderGoodsSerialzier(serializers.ModelSerializer):
    """
        订单商品表序列化器
    """
    sku = SKUSerializer(read_only=True)

    class Meta:
        model = OrderGoods
        fields = ('count', 'price', 'sku')


class OrderSerializer(serializers.ModelSerializer):
    """
        详情订单序列化器
    """
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField()

    # 嵌套订单商品表返回
    skus = OrderGoodsSerialzier(read_only=True,many=True)

    class Meta:
        model = OrderInfo
        # fields = "__all__"
        exclude = ('address',)
