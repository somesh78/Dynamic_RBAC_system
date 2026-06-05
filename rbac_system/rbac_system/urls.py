"""
URL configuration for rbac_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet
from audits.views import AuditLogViewSet
from features.views import FeatureViewSet, RoleFeatureViewSet
from organizations.views import OrganizationViewSet
from roles.views import RoleViewSet

from .views import dashboard_view, roles_view, role_features_view, audit_logs_view

router = DefaultRouter()

router.register(r'accounts', UserViewSet)
router.register(r'audits', AuditLogViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'role_features', RoleFeatureViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("roles/", roles_view, name="roles"),
    path("role-features/", role_features_view, name="role-features"),
    path("audit-logs/", audit_logs_view, name="audit-logs")
]
