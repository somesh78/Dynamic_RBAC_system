from django.db.models.signals import post_save
from django.dispatch import receiver

from organizations.models import Organization
from roles.models import Role

@receiver(post_save, sender=Organization)
def create_default_roles(sender, instance, created, **kwargs):
    if created:
        default_roles=[
            'Super admin',
            'Admin',
            'Manager',
            'Employee'
            ]

        for role in default_roles:
            Role.objects.create(
                name=role, 
                organization=instance,
                is_default=True
            )