from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BasicTusiViewSet, BasicXiajingViewSet, BasicZhiguanViewSet, BasicZhudiViewSet,
    RelationshipTusiViewSet, RelationshipXiajingViewSet, RelationshipZhiguanViewSet, RelationshipZhudiViewSet
)

# 使用 DefaultRouter 自动生成路由
router = DefaultRouter()
# 为每个 ViewSet 注册路由，DRF 会自动生成 /tusi/, /tusi/{id}/ 等路由
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
    # 这一行就是你的所有 DRF 接口，无需手动创建其他 api/create/ 路由
    path('', include(router.urls)),
]