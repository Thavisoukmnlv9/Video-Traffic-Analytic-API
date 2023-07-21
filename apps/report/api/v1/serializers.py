from rest_framework import serializers
from apps.report.models import Report
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField


class ReportSerializer(serializers.ModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )

    image = HyperlinkedSorlImageField('1024')
    class Meta:
        model = Report
        fields = ['id','color', 'district', 'image', 'thumbnail']
