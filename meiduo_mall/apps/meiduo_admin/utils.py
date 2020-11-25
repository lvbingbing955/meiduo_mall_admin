from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'id' : user.id,
        'username':user.username

    }


class PageNum(PageNumberPagination):
    """
        定义分页器
    """
    page_size = 5  # 在没有指定每页返回数量的情况下，后端指定返回五条数据
    page_size_query_param = 'pagesize' # 指定控制每页显示数量的参数
    max_page_size = 10

    # 改写分页结果返回方法
    def get_paginated_response(self, data):
        return Response(
            {
                'count':self.page.paginator.count,
                'lists':data,
                'page' : self.page.number,  # 获取当前页码
                'pages':self.page.paginator.num_pages,
                'pagesize':self.page_size
            }
        )