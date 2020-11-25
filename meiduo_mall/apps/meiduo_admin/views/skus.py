from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.skus import SKUSerializer
from meiduo_admin.utils import PageNum
from goods.models import SKU


class SKUViewSet(ModelViewSet):
    """
        SKU表数据的增删改查
    """
    serializer_class = SKUSerializer
    queryset = SKU.objects.all()
    pagination_class = PageNum
