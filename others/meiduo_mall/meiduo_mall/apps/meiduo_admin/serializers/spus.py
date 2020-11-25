from rest_framework import serializers

from goods.models import SPU, Brand,GoodsCategory


class SPUSerializer(serializers.ModelSerializer):
    """
        SPU表序列化器
    """
    # 品牌
    brand_id = serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)

    # 分类数据
    category1 = serializers.StringRelatedField(read_only=True)
    category2 = serializers.StringRelatedField(read_only=True)
    category3 = serializers.StringRelatedField(read_only=True)
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        fields = '__all__'





class BrandSerializer(serializers.ModelSerializer):
    """
        品牌序列化器
    """

    class Meta:
        model = Brand
        fields = '__all__'


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
        分类序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = '__all__'
