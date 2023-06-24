from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение, которое позволяет только владельцу объекта выполнять операции записи.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить любые операции чтения (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверить, является ли пользователь владельцем объекта
        return obj.user == request.user