from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from fdfs_client.client import Fdfs_client
from goods.models import SKUImage, SKU
from meiduo_admin.serializers.image import ImageSerializer, SKUSerializer

from meiduo_admin.utils import PageNum


class ImageView(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = SKUImage.objects.all()
    pagination_class = PageNum

    def simple(self, request):
        # 获取图片所关联的sku商品信息
        data = SKU.objects.all()

        # 序列化返回

        ser = SKUSerializer(data, many=True)

        return Response(ser.data)

    # 重写父类保存业务逻辑，上传到fastDFS中
    def create(self, request, *args, **kwargs):

        # 获取sku的id进行验证

        sku_id = request.data.get('sku')[0]

        try:
            sku=SKU.objects.get(sku_id=sku_id)
        except:
            return Response(status=500)


        # 1、获取图片数据
        data = request.FILES.get('image')
        # 验证图片数据
        if data is None:
            return Response(status=500)


        # 2、建立fastDFS连接对象
        client = Fdfs_client(settings.FASTDFS_PATH)

        # 3、上传图片
        res = client.upload_by_buffer(data.read())

        # 4、判断上传状态
        if res['Status'] != 'Upload successed.':
            return Response({'error': '上传失败'}, status=501)

        # 5、保存上传的图片路径
        image_url = res['Remote file_id']

        img = SKUImage.objects.create(sku_id=sku_id, image=image_url)

        # 6、结果返回
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },

            status=201
        )

    # 重写父类更新业务逻辑，上传到fastDFS中
    def update(self, request, *args, **kwargs):

        # 1、获取图片数据
        data = request.FILES.get('image')

        # 2、建立fastDFS连接对象
        client = Fdfs_client(settings.FASTDFS_PATH)

        # 3、上传图片
        res = client.upload_by_buffer(data.read())

        # 4、判断上传状态
        if res['Status'] != 'Upload successed.':
            return Response({'error': '上传失败'}, status=501)

        # 5、更新上传的图片路径
        image_url = res['Remote file_id']
        # 获取更新的图片对象
        img = self.get_object()
        sku_id = request.data.get('sku')[0]
        img.sku_id = sku_id
        img.image = image_url
        img.save()

        # 6、结果返回
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },

            status=201
        )
