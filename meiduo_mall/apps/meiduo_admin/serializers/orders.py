from rest_framework import serializers
from orders.models import OrderInfo


class OrdersSerializer(serializers.ModelSerializer):
    """
        订单序列化器
    """

    class Meta:
        model = OrderInfo
        fields = ('order_id','create_time')