from rest_framework import serializers

from goods.models import SPUSpecification


class SPUSpecificationSerializer(serializers.ModelSerializer):
    """
       SPUSpecification表序列化器
    """
    spu=serializers.StringRelatedField(read_only=True)
    spu_id=serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = '__all__'
