from rest_framework.response import Response
from  rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Group,Permission

from meiduo_admin.serializers.group import GroupSerialzier
from meiduo_admin.serializers.permission import PermissionSerialzier
from meiduo_admin.utils import PageNum


class GroupView(ModelViewSet):
    serializer_class = GroupSerialzier
    queryset = Group.objects.all()
    pagination_class = PageNum


    def simple(self,request):
        # 获取所有权限
        data=Permission.objects.all()

        # 序列化返回所有权限
        ser=PermissionSerialzier(data,many=True)

        return Response(ser.data)
