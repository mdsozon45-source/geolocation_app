from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LocationAPIView(APIView):
	
    def post(self, request):
        data = request.data.copy()
        ip_address = request.META.get('REMOTE_ADDR', '') 
        data['ip_address'] = ip_address
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LocationDataView(TemplateView):
    template_name = 'position.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context