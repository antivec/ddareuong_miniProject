from distutils.log import debug
from django.shortcuts import render
from urllib3 import HTTPResponse
from dda_db.models import dda_db
from django.http import HttpResponse
from urllib.request import urlopen,Request
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import sqlite3
import json
import requests as req
import pickle



class MainpageView(TemplateView):
    template_name = 'jquery.html'
# Create your views here.
    def index(request):
        return render(request, 'jquery.html')

@csrf_exempt
def db_save(request):
    url = "http://openapi.seoul.go.kr:8088/4f4557774d776f6431323044696f6a77/json/bikeList/1/6"  #1에서 n개 index 요청
    result = "DB Updated!!"
    if request.method == 'POST':
        try: #예외처리
            my_req = Request(url)
            my_req.get_method = lambda : 'GET'
            data = urlopen(my_req).read()
            Dda_row = json.loads(data)['rentBikeStatus']['row']

            for objs in Dda_row:                    
                _rackToint = objs['rackTotCnt']
                _stationName = objs['stationName']
                _parkingBikeToCnt = objs['parkingBikeTotCnt']
                _shared = objs['shared']
                _stationLatitude = objs['stationLatitude']
                _stationLongitude = objs['stationLongitude']
                _stationId = objs['stationId']
                to_Dda_db = dda_db(
                rackToint = _rackToint, 
                stationName = _stationName,
                    parkingBikeToCnt = _parkingBikeToCnt,
                    shared = _shared,
                    stationLatitude = _stationLatitude,
                    stationLongitude = _stationLongitude,
                    stationId = _stationId)

                if dda_db.objects.filter(stationName = _stationName).exists() == False:                                  
                    to_Dda_db.save()
                else:
                    dda_db.objects.get(stationName = _stationName)
                    dda_db.rackToint = _rackToint
                    dda_db.parkingBikeToCnt = _parkingBikeToCnt
                    dda_db.shared = _shared
                    dda_db.stationLatitude = _stationLatitude
                    dda_db.stationLongitude = _stationLongitude
                    dda_db.stationId = _stationId
                    dda_db.save()

        except Exception as e:
            result = "Error Occured !! ({0})".format(e)
    return HttpResponse(result)

@csrf_exempt
def db_select(data):
    db_conn = sqlite3.connect('./db.sqlite3')
    cursor = db_conn.cursor()
    query = ("Select stationName from DDA_DB where name LIKE %{0} ").format(data)
    cursor.execute(query)
