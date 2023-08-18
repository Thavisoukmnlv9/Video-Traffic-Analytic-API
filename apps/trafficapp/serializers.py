from rest_framework import serializers
from .models import DataAnaly

class DataAnalySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnaly
        fields = ('id', 'images', 'num_plate', 'bland', 'color', 'color_plate', 'province', 'Date')