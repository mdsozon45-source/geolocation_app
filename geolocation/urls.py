from django.urls import path
from .views import LocationAPIView,LocationDataView

urlpatterns = [
    path('api/location/', LocationAPIView.as_view(), name='location-api'),

    path('location-data/', LocationDataView.as_view(), name='location-data')
]
