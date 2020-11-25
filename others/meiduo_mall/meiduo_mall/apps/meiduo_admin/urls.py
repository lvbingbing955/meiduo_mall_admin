from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from .views import increments,user,skus,spus,specs,options,orders,channels,brands,image,permission,group,admin

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


# ------------------------------ SKU路由------------------------------------------------
    # 获取三级分类
    url(r'^skus/categories/$', skus.SKUViewSet.as_view({'get':'categorie'})),
    # 获取spu数据
    url(r'^goods/simple/$', skus.SKUViewSet.as_view({'get':'goodssimple'})),
    # 获取spu规格数据
    url(r'^goods/(?P<pk>\d+)/specs/$', skus.SKUViewSet.as_view({'get':'spuspecification'})),
#-------------------------------SPU路由--------------------------------------
    # 获取品牌数据
    url(r'^goods/brands/simple/$', spus.SPUSView.as_view({'get': 'brand'})),
    # 获取一级分类数据
    url(r'^goods/channel/categories/$', spus.SPUSView.as_view({'get': 'channel'})),
    # 获取二级和三级分类数据
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', spus.SPUSView.as_view({'get': 'channels'})),


#-------------------------------规格选项表路由--------------------------------------

    url(r'^goods/specs/simple/$', options.SpecificationOptionView.as_view({'get': 'simple'})),


#-------------------------------订单表路由--------------------------------------
    # url(r'^orders/$', orders.OrdersView.as_view()),
    # url(r'^orders/(?P<pk>\d+)/$', orders.OrderView.as_view()),



    url(r'^goods/channel_types/$', channels.ChannelView.as_view({'get':'channel_types'})),
    url(r'^goods/categories/$', channels.ChannelView.as_view({'get':'categories'})),


    url(r'^skus/simple/$', image.ImageView.as_view({'get':'simple'})),


# ---------------------权限类型匹配-----------------
    url(r'^permission/content_types/$', permission.PermisssionView.as_view({'get':'content_types'})),



    url(r'^permission/simple/$', group.GroupView.as_view({'get':'simple'})),

    url(r'^permission/groups/simple/$', admin.AdminView.as_view({'get':'simple'})),






]

rotue= DefaultRouter()
rotue.register('skus/images',image.ImageView,base_name='images')
urlpatterns += rotue.urls
#------------------------------ SKU表路由------------------------------------------------
rotue= DefaultRouter()
rotue.register('skus',skus.SKUViewSet,base_name='skus')
urlpatterns += rotue.urls


#------------------------------ SPUSpecification表路由-----------------------------------
rotue= DefaultRouter()
rotue.register('goods/specs',specs.SPUSpecificationView,base_name='specs')
urlpatterns += rotue.urls

#------------------------------ 商品频道表路由-----------------------------------
rotue= DefaultRouter()
rotue.register('goods/channels',channels.ChannelView,base_name='channels')
urlpatterns += rotue.urls


rotue= DefaultRouter()
rotue.register('goods/brands',brands.BrandView,base_name='brands')
urlpatterns += rotue.urls


#------------------------------ SPU表路由------------------------------------------------
rotue= DefaultRouter()
rotue.register('goods',spus.SPUSView,base_name='spus')
urlpatterns += rotue.urls


#------------------------------ 规格选项表路由------------------------------------------------
rotue= DefaultRouter()
rotue.register('specs/options',options.SpecificationOptionView,base_name='options')
urlpatterns += rotue.urls


#-------------------------------订单表路由--------------------------------------
rotue= DefaultRouter()
rotue.register('orders',orders.OrderViewSet,base_name='orders')
urlpatterns += rotue.urls



# -------------------------------权限表路由--------------------------------------

rotue= DefaultRouter()
rotue.register('permission/perms',permission.PermisssionView,base_name='perms')
urlpatterns += rotue.urls
# -------------------------------分组表路由--------------------------------------

rotue= DefaultRouter()
rotue.register('permission/groups',group.GroupView,base_name='groups')
urlpatterns += rotue.urls



# -------------------------------管理员表路由--------------------------------------

rotue= DefaultRouter()
rotue.register('permission/admins',admin.AdminView,base_name='admins')
urlpatterns += rotue.urls