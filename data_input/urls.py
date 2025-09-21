# data_input/urls.py

# 导入
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    BasicTusiViewSet, BasicXiajingViewSet, BasicZhiguanViewSet, BasicZhudiViewSet,
    RelationshipTusiViewSet, RelationshipXiajingViewSet, RelationshipZhiguanViewSet, RelationshipZhudiViewSet
)


# 使用 DefaultRouter 自动生成路由
router = DefaultRouter()
router.register(r'tusi', BasicTusiViewSet)
router.register(r'xiajing', BasicXiajingViewSet)
router.register(r'zhiguan', BasicZhiguanViewSet)
router.register(r'zhudi', BasicZhudiViewSet)
router.register(r'tusi-relationship', RelationshipTusiViewSet)
router.register(r'xiajing-relationship', RelationshipXiajingViewSet)
router.register(r'zhiguan-relationship', RelationshipZhiguanViewSet)
router.register(r'zhudi-relationship', RelationshipZhudiViewSet)


# 合并所有路由
urlpatterns = [
    # 你的原始路由
    path('api/create/<str:model_name>/', views.create_data, name='create_data_api'),

    # 新添加的 REST framework 路由
    path('', include(router.urls)),
]