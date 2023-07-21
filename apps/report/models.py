from django.db import models

class Report(models.Model):

    color = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("report")
    verbose_name_plural = ("reports")
