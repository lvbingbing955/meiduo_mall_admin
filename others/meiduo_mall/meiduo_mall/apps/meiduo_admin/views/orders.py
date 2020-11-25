from rest_framework.decorators import action
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from meiduo_admin.serializers.orders import OrdersSerializer, OrderSerializer
from orders.models import OrderInfo
from meiduo_admin.utils import PageNum


# class OrdersView(ListAPIView):
#     """
#         获取所有订单信息
#     """
#     serializer_class = OrdersSerializer
#     queryset = OrderInfo.objects.all()
#     pagination_class = PageNum
#
#
# class OrderView(RetrieveAPIView):
#
#     """
#         获取订单详情信息
#     """
#     serializer_class = OrderSerializer
#     queryset =OrderInfo.objects.all()

class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderInfo.objects.all()
    pagination_class = PageNum

    @action(methods=['put'],detail=True)
    def status(self,request,pk):

        # 获取订单对象和修改的状态值
        order=self.get_object()
        status=request.data.get('status')
        # 修改订单状态
        order.status=status
        order.save()
        ser = self.get_serializer(order)
        return Response(ser.data)
