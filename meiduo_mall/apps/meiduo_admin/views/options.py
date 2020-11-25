from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from meiduo_admin.serializers.options import SpecificationOptionSerializer, SPUSpecificationSerializer
from meiduo_admin.utils import PageNum
from goods.models import SpecificationOption,SPUSpecification


class SpecificationOptionView(ModelViewSet):
    """
        SPUSpecification表的增删改查
    """
    serializer_class = SpecificationOptionSerializer
    queryset = SpecificationOption.objects.all()
    pagination_class = PageNum


    def simple(self,requet):
        # 获取规格选项所对应的规格数据
        data=SPUSpecification.objects.all()

        # 序列化返回
        ser= SPUSpecificationSerializer(data,many=True)

        return Response(ser.data)

