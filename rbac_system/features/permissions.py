from rest_framework.permissions import BasePermission
from .models import RoleFeature


class HasFeature(BasePermission):

    feature_code = None

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if not request.user.role:
            return False

        return RoleFeature.objects.filter(
            role=request.user.role,
            feature__code=self.feature_code,
            enabled=True
        ).exists()


class ReportsPermission(HasFeature):
    feature_code = "reports"