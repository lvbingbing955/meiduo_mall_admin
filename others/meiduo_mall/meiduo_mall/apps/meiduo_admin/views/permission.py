from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# 权限模型类
from django.contrib.auth.models import Permission, ContentType

from meiduo_admin.serializers.permission import PermissionSerialzier, ContentTypeSerialzier
from meiduo_admin.utils import PageNum


class PermisssionView(ModelViewSet):
    serializer_class = PermissionSerialzier
    queryset = Permission.objects.all()
    pagination_class = PageNum

    def content_types(self, request):
        # 获取所有权限类型
        data = ContentType.objects.all()

        # 序列化返回权限类型
        ser = ContentTypeSerialzier(data, many=True)

        return Response(ser.data)
