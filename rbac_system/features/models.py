from django.db import models
from roles.models import Role

# Create your models here.
class Feature(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoleFeature(models.Model):
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE
    )
    feature = models.ForeignKey(
        Feature, on_delete=models.CASCADE
    )
    enabled = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('role', 'feature')