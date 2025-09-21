from django.urls import path
from . import views

urlpatterns = [
    # API 路由，接受 POST 请求，动态处理所有表的创建
    path('api/create/<str:model_name>/', views.create_data, name='create_data_api'),
]
