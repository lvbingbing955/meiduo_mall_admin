from rest_framework import serializers

from goods.models import SpecificationOption, SPUSpecification


class SpecificationOptionSerializer(serializers.ModelSerializer):
    """
       SpecificationOption表序列化器 规格选项
    """
    # 返回规格选项所关联的规格名称
    spec=serializers.StringRelatedField(read_only=True)
    # 返回规格选项所关联的规格id
    spec_id=serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = '__all__'

class SPUSpecificationSerializer(serializers.ModelSerializer):
    """
       SPUSpecification表序列化器
    """
    spu=serializers.StringRelatedField(read_only=True)
    spu_id=serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = '__all__'



