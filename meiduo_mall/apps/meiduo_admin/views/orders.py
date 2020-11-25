from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from meiduo_admin.serializers.orders import OrdersSerializer
from orders.models import OrderInfo
from meiduo_admin.utils import PageNum


class OrdersView(ListAPIView):
    """
        获取所有订单信息
    """
    serializer_class = OrdersSerializer
    queryset = OrderInfo.objects.all()
    pagination_class = PageNum
