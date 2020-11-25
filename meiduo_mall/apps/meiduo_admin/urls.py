from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from .views import increments,user,skus,spus,specs,options,orders

urlpatterns = [
    # JWT 完成登录
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户总量统计
    url(r'^statistical/total_count/$',increments.IncrementTotalcountView.as_view() ),
    # 当天注册用户总量统计
    url(r'^statistical/day_increment/$', increments.IncrementDayCountView.as_view()),
    # 当天登录用户总量统计
    url(r'^statistical/day_active/$', increments.IncrementDayActiveView.as_view()),
    # 当天下单用户总量统计
    url(r'^statistical/day_orders/$', increments.IncrementDayOrderView.as_view()),
    # 获取单月每天注册用户数量统计
    url(r'^statistical/month_increment/$', increments.IncrementMonthCountView.as_view()),
    # 获取当天分类数量统计
    url(r'^statistical/goods_day_views/$', increments.GoodsVisitCountView.as_view()),

#------------------------------ 用户路由------------------------------------------------

    # 获取所有用户
    url(r'^users/$', user.UserView.as_view()),


#-------------------------------规格选项表路由--------------------------------------

    url(r'^goods/specs/simple/$', options.SpecificationOptionView.as_view({'get': 'simple'})),


#-------------------------------订单表路由--------------------------------------
    url(r'^orders/$', orders.OrdersView.as_view()),

]
#------------------------------ SKU表路由------------------------------------------------
rotue= DefaultRouter()
rotue.register('skus',skus.SKUViewSet)
# rotue.register('skus',skus.SKUViewSet,base_name='skus')
urlpatterns += rotue.urls


#------------------------------ SPUSpecification表路由-----------------------------------
rotue= DefaultRouter()
rotue.register('goods/specs',specs.SPUSpecificationView)
urlpatterns += rotue.urls

#------------------------------ SPU表路由------------------------------------------------
rotue= DefaultRouter()
rotue.register('goods',spus.SPUSView)
urlpatterns += rotue.urls


#------------------------------ 规格选项表路由------------------------------------------------
rotue= DefaultRouter()
rotue.register('specs/options',options.SpecificationOptionView)
urlpatterns += rotue.urls