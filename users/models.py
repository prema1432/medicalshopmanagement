from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('shop', 'Shop'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(pre_save, sender=CustomUser)
def update_username(sender, instance, **kwargs):
    if not instance.is_superuser:
        if instance.role == 'customer':
            instance.username = generate_username('CU', instance)
        elif instance.role == 'admin':
            instance.username = generate_username('AD', instance)
        elif instance.role == 'shop':
            instance.username = generate_username('SH', instance)


def generate_username(prefix, instance):
    instance_id = instance.id
    username = f"{prefix}{instance_id:06d}"
    return username
