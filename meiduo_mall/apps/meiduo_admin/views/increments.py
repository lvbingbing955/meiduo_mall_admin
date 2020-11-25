from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from datetime import date, timedelta

from meiduo_admin.serializers.increment import GoodsVisitCountSerializer
from users.models import User
from goods.models import GoodsVisitCount


class IncrementTotalcountView(APIView):
    """
        注册用户总量统计
    """
    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1、查询注册用户总量
        count = User.objects.all().count()

        # 2、获取当前日期
        now_date = date.today()

        # 3、返回结果
        return Response({
            'count': count,
            'date': now_date
        })


class IncrementDayCountView(APIView):
    """
        获取当天注册用户总量统计
    """
    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1、获取当前日期
        now_date = date.today()
        # 2、查询当天注册用户总量
        count = User.objects.filter(date_joined__gte=now_date).count()
        # 3、返回结果
        return Response({
            'count': count,
            'date': now_date
        })


class IncrementDayActiveView(APIView):
    """
        获取当天登录用户总量统计
    """
    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1、获取当前日期
        now_date = date.today()
        # 2、查询当天登录用户总量
        count = User.objects.filter(last_login__gte=now_date).count()
        # 3、返回结果
        return Response({
            'count': count,
            'date': now_date
        })


class IncrementDayOrderView(APIView):
    """
        获取当天下单用户总量统计
    """
    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1、获取当前日期
        now_date = date.today()
        # 2、查询当天登录用户总量
        count = User.objects.filter(orders__create_time__gte=now_date).count()
        # 3、返回结果
        return Response({
            'count': count,
            'date': now_date
        })


class IncrementMonthCountView(APIView):
    """
        获取单月每天注册用户数量统计
    """
    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1、获取当前日期
        now_date = date.today()
        # 2、获取一个月前的日期
        start_date = now_date - timedelta(days=29)

        # 构建列表数据
        data_list = []
        for i in range(30):
            # 获取起始时间
            index_date = start_date + timedelta(days=i)
            # 获取第二天实现
            next_date = index_date + timedelta(days=1)
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=next_date).count()
            data_list.append({'count': count, 'date': index_date})
        # 3、返回结果
        return Response(data_list)


class GoodsVisitCountView(APIView):
    """
        获取当天分类数量统计
    """
    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1、获取当前日期
        now_date = date.today()
        # 2、查询当天登录用户总量
        goodvisit = GoodsVisitCount.objects.filter(date__gte=now_date)
        # 3、返回结果
        ser = GoodsVisitCountSerializer(goodvisit, many=True)
        return Response(ser.data)
