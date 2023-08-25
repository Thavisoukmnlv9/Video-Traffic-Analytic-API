from rest_framework import serializers
from apps.video.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['location_name', 'video']
