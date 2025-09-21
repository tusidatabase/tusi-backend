from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db import models as django_models
from . import models
import json

from rest_framework import viewsets
from .models import (
    BasicTusi, BasicXiajing, BasicZhiguan, BasicZhudi,
    RelationshipTusi, RelationshipXiajing, RelationshipZhiguan, RelationshipZhudi
)
from .serializers import (
    BasicTusiSerializer, BasicXiajingSerializer, BasicZhiguanSerializer, BasicZhudiSerializer,
    RelationshipTusiSerializer, RelationshipXiajingSerializer, RelationshipZhiguanSerializer, RelationshipZhudiSerializer
)


@csrf_exempt
@require_POST
def create_data(request, model_name):
    """
    一个通用的 API 视图，用于根据模型名称动态创建数据。
    它接收一个 POST 请求，请求体为 JSON 格式。
    """
    # 动态获取对应的模型类
    model_class = getattr(models, model_name, None)

    # 如果模型不存在，返回 404 错误
    if not model_class:
        return JsonResponse({'error': 'Model not found.'}, status=404)

    # 从请求体中解析 JSON 数据
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    # 准备创建实例的字段数据
    instance_data = {}

    try:
        # 遍历模型的所有字段，从 JSON 数据中获取对应的值
        for field in model_class._meta.get_fields():
            field_name = field.name

            # 排除自动生成的 ID 字段和关系字段
            if field.auto_created or isinstance(field,
                                                django_models.AutoField) or field_name == f'{model_class._meta.model_name}_id':
                continue

            # 处理外键关系
            if isinstance(field, django_models.ForeignKey):
                related_id = data.get(field_name)
                if related_id:
                    related_model = field.related_model
                    try:
                        # 根据 ID 查找关联实例
                        related_instance = related_model.objects.get(pk=related_id)
                        instance_data[field_name] = related_instance
                    except related_model.DoesNotExist:
                        return JsonResponse(
                            {'error': f'Related {related_model.__name__} with ID {related_id} not found.'}, status=404)
                # 允许外键字段为空
                elif field.null:
                    instance_data[field_name] = None
                else:
                    return JsonResponse({'error': f'Missing value for foreign key: {field_name}.'}, status=400)
            else:
                # 获取其他字段的值
                value = data.get(field_name)
                # 检查是否为必填字段
                if not field.null and value is None:
                    return JsonResponse({'error': f'Missing required field: {field_name}.'}, status=400)
                instance_data[field_name] = value

        # 使用处理好的数据创建并保存新的模型实例
        instance = model_class.objects.create(**instance_data)

        # 返回成功响应，包含新创建实例的 ID
        return JsonResponse({
            'success': True,
            'message': f'Successfully created {model_name}.',
            'id': getattr(instance, f'{model_name}_id', None)
        }, status=201)

    except Exception as e:
        return JsonResponse({'error': f'Failed to create instance: {e}'}, status=400)


class BasicTusiViewSet(viewsets.ModelViewSet):
    queryset = BasicTusi.objects.all()
    serializer_class = BasicTusiSerializer

class BasicXiajingViewSet(viewsets.ModelViewSet):
    queryset = BasicXiajing.objects.all()
    serializer_class = BasicXiajingSerializer

class BasicZhiguanViewSet(viewsets.ModelViewSet):
    queryset = BasicZhiguan.objects.all()
    serializer_class = BasicZhiguanSerializer

class BasicZhudiViewSet(viewsets.ModelViewSet):
    queryset = BasicZhudi.objects.all()
    serializer_class = BasicZhudiSerializer

class RelationshipTusiViewSet(viewsets.ModelViewSet):
    queryset = RelationshipTusi.objects.all()
    serializer_class = RelationshipTusiSerializer

class RelationshipXiajingViewSet(viewsets.ModelViewSet):
    queryset = RelationshipXiajing.objects.all()
    serializer_class = RelationshipXiajingSerializer

class RelationshipZhiguanViewSet(viewsets.ModelViewSet):
    queryset = RelationshipZhiguan.objects.all()
    serializer_class = RelationshipZhiguanSerializer

class RelationshipZhudiViewSet(viewsets.ModelViewSet):
    queryset = RelationshipZhudi.objects.all()
    serializer_class = RelationshipZhudiSerializer
