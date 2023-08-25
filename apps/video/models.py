from django.db import models

class Video(models.Model):
    location_name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/') 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.location_name
