from .models import AuditLog


def create_audit_log(actor,organization,action,target_type,target_id):

    AuditLog.objects.create(
        actor=actor,
        organization=organization,
        action=action,
        target_type=target_type,
        target_id=target_id
    )