from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.skus import SKUSerializer, CategorieSerialzier, GoodsSimpleSerialzier, \
    SPUSpecificationSerializer
from meiduo_admin.utils import PageNum
from goods.models import SKU,GoodsCategory,SPU,SPUSpecification



class SKUViewSet(ModelViewSet):
    """
        SKU表数据的增删改查
    """
    serializer_class = SKUSerializer
    queryset = SKU.objects.all()
    pagination_class = PageNum

    def categorie(self,request):
        #1、查询三级分类信息
        data=GoodsCategory.objects.filter(subs=None)

        # 序列化返回三级分类
        ser =CategorieSerialzier(data,many=True)

        return Response(ser.data)


    def goodssimple(self,request):
        # 查询spu表数据
        data=SPU.objects.all()
        # 序列化返回三级分类
        ser=GoodsSimpleSerialzier(data,many=True)
        return Response(ser.data)



    def spuspecification(self,request,pk):
        # 查询spu商品的所有规格
        data=SPUSpecification.objects.filter(spu_id=pk)

        # 序列化返回
        ser=SPUSpecificationSerializer(data,many=True)
        return Response(ser.data)

