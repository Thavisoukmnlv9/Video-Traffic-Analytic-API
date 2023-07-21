from django.db import models
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete

class Report(models.Model):

    color = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("report")
    verbose_name_plural = ("reports")


def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)
