from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from meiduo_admin.serializers.specs import SPUSpecificationSerializer
from meiduo_admin.utils import PageNum
from goods.models import SPUSpecification


class SPUSpecificationView(ModelViewSet):
    """
        SPUSpecification表的增删改查
    """
    serializer_class = SPUSpecificationSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = PageNum
