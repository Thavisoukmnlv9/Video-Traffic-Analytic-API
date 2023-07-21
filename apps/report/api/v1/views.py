
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ReportSerializer
from apps.report.models import Report
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


class ListCreateAPIView(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    parser_classes = (MultiPartParser, FormParser)
    

    @swagger_auto_schema(manual_parameters=[])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Report.objects.all()
        return queryset

class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    parser_classes = (MultiPartParser, FormParser)
    
