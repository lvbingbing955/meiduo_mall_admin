from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from meiduo_admin.serializers.channels import GoodsChannelSerialzier, GoodsCategorySerialzier, \
    GoodsChannelGroupSerialzier
from meiduo_admin.utils import PageNum
from goods.models import GoodsChannel, GoodsCategory, GoodsChannelGroup


class ChannelView(ModelViewSet):
    serializer_class = GoodsChannelSerialzier
    queryset = GoodsChannel.objects.all()
    pagination_class = PageNum

    def categories(self, request):
        # 获取一级分类数据
        data = GoodsCategory.objects.filter(parent=None)

        # 序列化返回
        ser = GoodsCategorySerialzier(data, many=True)

        return Response(ser.data)

    def channel_types(self, request):
        # 获取频道组数据
        data = GoodsChannelGroup.objects.all()
        # 序列化返回
        ser = GoodsChannelGroupSerialzier(data, many=True)

        return Response(ser.data)
