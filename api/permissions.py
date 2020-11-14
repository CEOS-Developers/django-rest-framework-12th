from rest_framework import permissions
from rest_framework.permissions import BasePermission

#카트는 로그인한 유저에게만 보여지도록
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


#상품&카테고리 등록 및 삭제는 스태프에게만 허용
class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #GET, HEAD, OPTION(수정 삭제 삽입 제외)
            return True
        else:
            return request.user.is_staff
