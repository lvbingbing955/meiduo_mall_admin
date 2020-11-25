from rest_framework import serializers
from django.contrib.auth.models import Permission,ContentType


class PermissionSerialzier(serializers.ModelSerializer):
    """
        权限表序列化器
    """
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerialzier(serializers.ModelSerializer):
    """
        权限类型序列化器
    """
    class Meta:
        model = ContentType
        fields = '__all__'

