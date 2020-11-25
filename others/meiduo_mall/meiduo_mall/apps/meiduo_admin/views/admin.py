from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import Group
from meiduo_admin.serializers.admin import AdminSerialzier
from meiduo_admin.serializers.group import GroupSerialzier
from users.models import User
from meiduo_admin.utils import PageNum


class AdminView(ModelViewSet):
    serializer_class = AdminSerialzier
    queryset = User.objects.filter(is_staff=True)
    pagination_class = PageNum


    def simple(self,reqeust):
        # 获取分组信息
        data=Group.objects.all()

        # 分组信息返回
        ser=GroupSerialzier(data,many=True)

        return Response(ser.data)
