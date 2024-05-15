from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderInsufficientPrivileges
from geopy.geocoders import OpenCage


# class LocationAPIView(APIView):

#     def post(self, request):
#         latitude = request.data.get('latitude')
#         longitude = request.data.get('longitude')

#         # Initialize geocoder with API key
#         geolocator = Nominatim(user_agent="geoapiExercises")
#         location = geolocator.reverse(str(latitude) + "," + str(longitude))
        
#         address = location.raw['address']

#         city = address.get('city', '')
#         state = address.get('state', '')
#         country = address.get('country', '')
#         country_code = address.get('country_code', '')

#         request.data['city'] = city
#         request.data['state'] = state
#         request.data['country'] = country
#         request.data['country_code'] = country_code
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LocationAPIView(APIView):
    def post(self, request):
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        geolocator = Nominatim(user_agent='geoapi')

        try:
            location = geolocator.reverse((latitude, longitude), exactly_one=True)
            address = location.address
            address2 = location.raw['address']
            
            city = address2.get('city', '')
            state = address2.get('state_district', '')
            country = address2.get('country', '')
            country_code = address2.get('country_code', '')
            village = address2.get('village', '')
            state_ = address2.get('state', '')
    		

            print('City : ',city)
            print('State : ',state)
            print('country : ',country)
            print('country_code : ',country_code)
            print('village : ',village)
            print('state_ : ',state_)
			
            request.data['city'] = city
            request.data['state'] = state
            request.data['country'] = country
            request.data['country_code'] = country_code
            serializer = LocationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocationDataView(TemplateView):
    template_name = 'position.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context