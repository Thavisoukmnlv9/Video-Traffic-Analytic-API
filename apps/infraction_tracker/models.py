from django.db import models
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


class InfractionTracker(models.Model):
    image_one = models.ImageField(
        verbose_name='ImageOne', upload_to='uploads/', blank=True, null=True
    )
    image_two = models.ImageField(
        verbose_name='ImageTwo', upload_to='uploads/', blank=True, null=True
    )
    vehicle_registration_number = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    vehicle_color = models.CharField(max_length=255)
    vehicle_registration_color = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Infraction Tracker"
        verbose_name_plural = "Infraction Tracker"


def sorl_delete(**kwargs):
    delete(kwargs['file'])

cleanup_pre_delete.connect(sorl_delete)
