from django.urls import resolvers
from django.shortcuts import render, redirect

from audits.models import AuditLog
from organizations.models import Organization
from accounts.models import User
from roles.models import Role

from features.models import Feature, RoleFeature

from audits.utils import create_audit_log

def dashboard_view(request):

    organizations = Organization.objects.all()
    org_data = []
    for org in organizations:
        org.user_count = User.objects.filter(organization=org).count()
        org_data.append(org)

    context = {
        "organizations_count": Organization.objects.count(),
        "users_count": User.objects.count(),
        "roles_count": Role.objects.count(),
        "recent_users": User.objects.select_related("organization", "role")[:10],
        "organizations": org_data,
    }
    return render(request, 'dashboard.html', context)

def audit_logs_view(request):
    logs = AuditLog.objects.select_related("actor", "organization").order_by("-created_at")

    context = {
        "logs":logs
    }
    return render(request, 'audit_logs.html', context)   

def roles_view(request):
    if request.method == "POST" and "delete" in request.GET:

        role_id = request.GET.get("delete")

        role = Role.objects.get(id=role_id)

        create_audit_log(
            actor=request.user,
            organization=role.organization,
            action="Role Deleted",
            target_type="Role",
            target_id=role.id
        )

        role.delete()

        return redirect("roles")


    if request.method == 'POST':
        role_name = request.POST.get("name")
        org_id = request.POST.get("organization")

        role = Role.objects.create(
            name=role_name,
            organization_id=org_id,
            is_default=(
                request.POST.get("is_default")=="on"
            )
        )
        create_audit_log(
            actor=request.user,
            organization=role.organization,
            action="Role Created",
            target_type="Role",
            target_id=role.id
        )
        return redirect("roles")
    
    roles = Role.objects.select_related("organization").all()
    organizations = Organization.objects.all()
    
    context = {
        "roles": roles,
        "organizations": organizations
    }
    return render(request, 'roles.html', context)

def role_features_view(request):
    roles = Role.objects.all()
    role_id = request.GET.get("role")
    selected_role = None
    features = []
    if role_id:
        selected_role = Role.objects.get(id = role_id)
        
        if request.method =="POST":
            selected_features = request.POST.getlist("features")
            RoleFeature.objects.filter(role=selected_role).delete()
            create_audit_log(
                actor=request.user,
                organization=selected_role.organization,
                action="Updated Role Features",
                target_type="Role",
                target_id=selected_role.id
            )
            
            for feature_id in selected_features:
                RoleFeature.objects.create(
                    role=selected_role,
                    feature_id=feature_id,
                    enabled=True
                )
        all_features = Feature.objects.all()

        for feature in all_features:
            feature.enabled = RoleFeature.objects.filter(
                role=selected_role,
                feature=feature,
                enabled=True
            ).exists()

            features.append(feature)
    context = {
        "roles": roles,
        "selected_role": selected_role,
        "features": features        
    }
    return render(request, 'role_features.html', context)