# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('data_input.urls')),
    path('api/auth/', include('accounts.urls')), # 将你的 accounts 路由包含在 api/auth/ 路径下
]