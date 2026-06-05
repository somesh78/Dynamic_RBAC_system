from django.db.models import CASCADE
from django.db import models

from organizations.models import Organization
from accounts.models import User

# Create your models here.
class AuditLog(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=CASCADE
    )
    actor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    action = models.CharField(max_length=255)
    target_type = models.CharField(max_length=100)
    target_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action