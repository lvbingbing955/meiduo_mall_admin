from rest_framework import serializers
from goods.models import SKU, SKUSpecification


class SKUSpecificationSerializer(serializers.ModelSerializer):
    """SKU具体规格 表序列化器"""
    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    # 返回关联spu表的名称和关联的分类表的名称
    spu = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    # 返回模型类类的spu_id和category_id
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()


    # 返回商品的规格信息 ，在商品规格详情表（SKUSpecification）中有个外键sku关了当前的SKU表
    specs = SKUSpecificationSerializer(many=True)

    class Meta:
        model = SKU
        fields = "__all__"
