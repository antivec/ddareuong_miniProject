from django.shortcuts import render
from dda_db.models import dda_db
from django.views.decorators.csrf import csrf_exempt
import json
import requests as req
@csrf_exempt
## variables
start_page = 1
end_page = 5
api_key = '4f4557774d776f6431323044696f6a77'
##
    # rackToint = models.IntegerField() # ID?
    # stationName = models.CharField(max_length= 32) # 대여소 이름
    # parkingBikeToCnt = models.IntegerField() # 대여소에 남아있는 자전거 수
    # shared = models.IntegerField() # 빌려간 수
    # stationLatitude = models.FloatField() # Lat
    # stationLongitude = models.FloatField() # Long
    # stationId = models.CharField(max_length= 32) 
# Create your views here.
response = req.get('http://openapi.seoul.go.kr:8088/{0}/json/bikeList/{1}/{2}/').format(api_key, start_page, end_page)
DdaReuong_data = json.loads(response.content.decode('UTF-8'))

rackToint = DdaReuong_data['rackToint']
stationName = DdaReuong_data['stationName']
parkingBikeToCnt = DdaReuong_data['parkingBikeToCnt']
shared = DdaReuong_data['shared']
stationLatitude = DdaReuong_data['stationLatitude']
stationLongitude = DdaReuong_data['stationLongitude']
stationId = DdaReuong_data['stationId']

to_Dda_db = dda_db(rackToint = rackToint, stationName = stationName,
parkingBikeToCnt = parkingBikeToCnt,
shared = shared,
stationLatitude = stationLatitude,
stationLongitude = stationLongitude,
stationId = stationId)

to_Dda_db.save()

def render_Dda_data(request):
    return render(request)