from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.brand import BrandSerialzier
from meiduo_admin.utils import PageNum
from goods.models import Brand


class BrandView(ModelViewSet):
    serializer_class = BrandSerialzier
    queryset = Brand.objects.all()
    pagination_class = PageNum


