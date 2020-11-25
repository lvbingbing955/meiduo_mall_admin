from rest_framework import serializers
from goods.models import SKU, SKUSpecification, GoodsCategory, SPU, SPUSpecification, SpecificationOption


class SKUSpecificationSerializer(serializers.ModelSerializer):
    """SKU具体规格 表序列化器"""

    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    """
        SKU表数据
    """
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

    def create(self, validated_data):
        # 1、保存sku表
        # self指的是当前序列化器对象，在self下面有个context属性保存了请求对象
        specs=self.context['request'].data.get('specs')
        # specs = validated_data['specs']
        # 因为sku表中没有specs字段，所以在保存的时候需要删除validated_data中specs数据
        del validated_data['specs']
        sku = SKU.objects.create(**validated_data)

        # 2、保存SKU具体规格
        for spec in specs:
            SKUSpecification.objects.create(sku=sku, spec_id=spec['spec_id'], option_id=spec['option_id'])

        return sku

    def update(self, instance, validated_data):
        # 1、保存sku表
        specs = self.context['request'].data.get('specs')

        instance.name=validated_data['name']
        instance.save()

        # 2、保存SKU具体规格
        for spec in specs:
            SKUSpecification.objects.create(sku=instance, spec_id=spec['spec_id'], option_id=spec['option_id'])

        return instance


class CategorieSerialzier(serializers.ModelSerializer):
    """
        分类序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')


class GoodsSimpleSerialzier(serializers.ModelSerializer):
    """
            spu序列化器
        """

    class Meta:
        model = SPU
        fields = ('id', 'name')


class SpecificationOptionSereializer(serializers.ModelSerializer):
    """
           商品规格选项序列化器
    """

    class Meta:
        model = SpecificationOption
        fields = "__all__"


class SPUSpecificationSerializer(serializers.ModelSerializer):
    """
        商品规格序列化器
    """
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    # 指定规格选项返回的内容
    options = SpecificationOptionSereializer(many=True, read_only=True)

    class Meta:
        model = SPUSpecification
        fields = '__all__'
