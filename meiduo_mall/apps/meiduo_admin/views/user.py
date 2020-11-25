from rest_framework.generics import ListCreateAPIView

from meiduo_admin.serializers.user import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User

class UserView(ListCreateAPIView):
    """
        获取用户对象和保存用户对象的
    """

    # queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNum


    def get_queryset(self):
        # 根据前端传递keyword参数查询不同的数据，获取keyword数据
        keyword=self.request.query_params.get('keyword')  # slef保存的有request对象
        if keyword == '' or keyword is None:
            # 如果keyword是空值，要获取所有数据
            return User.objects.all()

        else:
            return User.objects.filter(username=keyword)




