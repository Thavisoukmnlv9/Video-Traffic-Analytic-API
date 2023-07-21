from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/report', ListCreateAPIView.as_view(), name='reports'),
    path('api/v1/report/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='report'),
]
