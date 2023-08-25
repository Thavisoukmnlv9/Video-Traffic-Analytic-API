
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import InfractionTrackerSerializer
from apps.infraction_tracker.models import InfractionTracker
from rest_framework.parsers import MultiPartParser, FormParser

class ListCreateAPIView(ListCreateAPIView):
    queryset = InfractionTracker.objects.all()
    serializer_class = InfractionTrackerSerializer
    parser_classes = (MultiPartParser, FormParser)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = InfractionTracker.objects.all()
    serializer_class = InfractionTrackerSerializer
    parser_classes = (MultiPartParser, FormParser)