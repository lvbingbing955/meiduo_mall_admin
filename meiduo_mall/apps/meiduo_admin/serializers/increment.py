from rest_framework import serializers
from goods.models import GoodsVisitCount

class GoodsVisitCountSerializer(serializers.ModelSerializer):
    # 关联嵌套返回分类名字
    category=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=GoodsVisitCount
        fields="__all__"