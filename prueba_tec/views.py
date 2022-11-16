from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from prueba_tec.hotel_modules.hotel_modules import HotelsInfo
from .serializers import HotelSerializer
import json


class BasicAPI(APIView):
    
    def get(self, request):
        
        data = request.data
        res = HotelsInfo.last(data['hotels'],
                                data['dateFrom'],
                                data['dateTo'])
        data = {
            'DailyMinPrices': res['min_price_list'],
            'DailyMaxPrices': res['max_price_list'],
            'DailyAvgPrices': res['avg'],
            'MoreExpensiveHotel': res['max_price_data'],
            'CheapestHotel': res['min_price_data'],
            'MoreExpensiveDay': res['more_expensive_day']
        }
        
        results = HotelSerializer(data, many=False).data

        return Response(results)
    
    def post(self, request):
        req_data = request.data
        data = {
            'hotels': req_data.get('hotels'),
            'dateFrom': req_data.get('dateFrom'),
            'dateTo': req_data.get('dateTo')
        }
        return Response(data, status=status.HTTP_200_OK)