from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsAdminUserOrReadOnly(IsAdminUser):

    def check_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin