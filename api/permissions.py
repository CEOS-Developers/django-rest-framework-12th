from rest_framework import permissions

#상품&카테고리 등록 및 삭제는 스태프에게만 허용
class IsStaffOrReadonly(permissions.BasePermission):
    #message = 'Adding, Deleting not allowed' -> 인증 부분 구현하지 않아서 확인불가 -> 인증 통과한 후, permission denied 실행

    def has_permission(self, request, view): #로그인에 상관없이 모두에게
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #GET, HEAD, OPTION(수정 삭제 삽입 제외)
            return True
        else:
            return request.user.is_staff
