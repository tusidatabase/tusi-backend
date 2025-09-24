# account/views.py
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.db import IntegrityError

INVITE_CODE = "7X9K2B8F3R6A"  # 注册邀请码


class RegisterView(APIView):
    """
    处理用户注册的API接口。
    """

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        invite = request.data.get("invite")

        if invite != INVITE_CODE:
            return Response({"message": "邀请码错误"}, status=status.HTTP_400_BAD_REQUEST)
        if not username or not password:
            return Response({"message": "用户名和密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_user = User.objects.create_user(username=username, password=password)
            return Response({"message": "注册成功", "username": new_user.username}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"message": "用户名已存在"}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({"message": f"注册失败: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(ObtainAuthToken):
    """
    处理用户登录的API接口，返回认证Token。
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


class LogoutView(APIView):
    """
    处理用户登出，删除Token。
    """

    def post(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
            return Response({"message": "登出成功"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "用户未登录"}, status=status.HTTP_400_BAD_REQUEST)