from django.urls import path
from trafficapp import readtext, img_analytic

urlpatterns = [
      
    path('apps/trafficapp', readtext, name='read'),    
      
]
