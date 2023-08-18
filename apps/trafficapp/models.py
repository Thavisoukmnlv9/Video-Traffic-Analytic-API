
from django.db import models
from colorfield.fields import ColorField

class DataAnaly(models.Model):
    images = models.ImageField(upload_to ='assets/img')
    num_plate = models.CharField(max_length=10)
    brand = models.TextField(max_length=255)
    color = ColorField(image_field="image")
    color_plate = ColorField()
    province = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

