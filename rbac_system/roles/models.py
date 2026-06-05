from organizations.models import Organization
from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    