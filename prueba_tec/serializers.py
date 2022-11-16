from django.contrib.auth.models import User, Group
from rest_framework import serializers

class HotelSerializer(serializers.Serializer):
   DailyMinPrices = serializers.ListField()
   DailyMaxPrices = serializers.ListField()
   DailyAvgPrices = serializers.ListField()
   MoreExpensiveHotel = serializers.CharField()
   CheapestHotel = serializers.CharField()
   MoreExpensiveDay = serializers.CharField()
   
   
   """ 
'DailyMinPrices': res['min_price_list'],
'DailyMaxPrices': res['max_price_list'],
'DailyAvgPrices': res['avg'],
'MoreExpensiveHotel': res['max_price_data'],
'CheapestHotel': res['min_price_data'],
'MoreExpensiveDay': res['more_expensive_day']
         """   
class YourSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   comments = serializers.IntegerField()
   likes = serializers.IntegerField()    

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']