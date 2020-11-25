from rest_framework import serializers
from goods.models import SKUImage,SKU


class ImageSerializer(serializers.ModelSerializer):
    sku = serializers.PrimaryKeyRelatedField(read_only=True)
    # sku_id=serializers.IntegerField()


    class Meta:
        model = SKUImage
        fields = "__all__"


    # def create(self, validated_data):
    #     image=SKUImage.objects.create(validated_data)
    #     return image




class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ('id','name')
