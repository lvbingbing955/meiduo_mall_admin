from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from meiduo_admin.serializers.spus import SPUSerializer, BrandSerializer, GoodsCategorySerializer
from meiduo_admin.utils import PageNum
from goods.models import SPU, Brand,GoodsCategory


class SPUSView(ModelViewSet):
    """
        spu表的增删改查
    """
    serializer_class = SPUSerializer
    queryset = SPU.objects.all()
    pagination_class = PageNum

    def brand(self, request):
        # 1、查询所有品牌数据
        data = Brand.objects.all()
        # 2、序列化返回品牌数据
        ser = BrandSerializer(data, many=True)

        return Response(ser.data)


    def channel(self,request):
        # 1、获取一级分类数据
        data = GoodsCategory.objects.filter(parent=None)
        # 2、序列化返回分类数据
        ser=GoodsCategorySerializer(data,many=True)
        return Response(ser.data)

    def channels(self,request,pk):
        # 1、获取二级和三级分类数据
        data = GoodsCategory.objects.filter(parent_id=pk)
        # 2、序列化返回分类数据
        ser=GoodsCategorySerializer(data,many=True)
        return Response(ser.data)

