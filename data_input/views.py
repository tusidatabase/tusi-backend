# data_input/views.py
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication # 导入 Token 认证
from .models import (
    BasicTusi, BasicXiajing, BasicZhiguan, BasicZhudi,
    RelationshipTusi, RelationshipXiajing, RelationshipZhiguan, RelationshipZhudi
)
from .serializers import (
    BasicTusiSerializer, BasicXiajingSerializer, BasicZhiguanSerializer, BasicZhudiSerializer,
    RelationshipTusiSerializer, RelationshipXiajingSerializer, RelationshipZhiguanSerializer,
    RelationshipZhudiSerializer
)


class BaseDataViewSet(viewsets.ModelViewSet):
    """
    一个基础的 ViewSet，用于处理通用的配置和权限控制。
    """
    # 权限控制：只允许已认证的用户访问，未认证用户只能只读
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 认证方式：使用 Token 认证
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """
        根据登录用户来过滤数据集，只显示用户自己提交的数据。
        """
        queryset = super().get_queryset()
        # 确保用户已登录，并且每条记录都有一个 'author' 字段
        if self.request.user.is_authenticated:
            # 过滤出 author 字段等于当前登录用户的记录
            return queryset.filter(author=self.request.user)
        # 如果用户未登录，则返回空结果集
        return queryset.none()

    def perform_create(self, serializer):
        """
        在创建新数据时，自动将当前登录用户设为 author。
        """
        serializer.save(author=self.request.user)


class BasicTusiViewSet(BaseDataViewSet):
    """
    土司基本信息
    """
    queryset = BasicTusi.objects.all()
    serializer_class = BasicTusiSerializer


class BasicXiajingViewSet(BaseDataViewSet):
    """
    辖境信息
    """
    queryset = BasicXiajing.objects.all()
    serializer_class = BasicXiajingSerializer


class BasicZhiguanViewSet(BaseDataViewSet):
    """
    职官信息
    """
    queryset = BasicZhiguan.objects.all()
    serializer_class = BasicZhiguanSerializer


class BasicZhudiViewSet(BaseDataViewSet):
    """
    驻地信息
    """
    queryset = BasicZhudi.objects.all()
    serializer_class = BasicZhudiSerializer


class RelationshipTusiViewSet(BaseDataViewSet):
    """
    土司关系表
    """
    queryset = RelationshipTusi.objects.all()
    serializer_class = RelationshipTusiSerializer


class RelationshipXiajingViewSet(BaseDataViewSet):
    """
    辖境关系表
    """
    queryset = RelationshipXiajing.objects.all()
    serializer_class = RelationshipXiajingSerializer


class RelationshipZhiguanViewSet(BaseDataViewSet):
    """
    职官关系表
    """
    queryset = RelationshipZhiguan.objects.all()
    serializer_class = RelationshipZhiguanSerializer


class RelationshipZhudiViewSet(BaseDataViewSet):
    """
    驻地关系表
    """
    queryset = RelationshipZhudi.objects.all()
    serializer_class = RelationshipZhudiSerializer