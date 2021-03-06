from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from .serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    """
    Используется для:
    - отображения всех аккаунтов в системе {'get':'list'}
    - создания нового пользователя {'post':'create'}

    С использованием идентификатора в URI:
    - отображение данных об аккаунте {'get':'retrieve'}
    - замены данных аккаунта на новые {'put':'update'}
    - частичное обновление данных аккаунта {'patch':'partial_update'}
    - удаление аккаунта из системы {'delete':'destroy'}
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
