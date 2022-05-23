from distutils.log import debug
from django.shortcuts import render
from dda_db.models import dda_db
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import sqlite3
import json
import requests as req


# url = "http://openapi.seoul.go.kr:8088/4f4557774d776f6431323044696f6a77/json/bikeList/1/3"

class MainpageView(TemplateView):
    template_name = 'jquery.html'
# Create your views here.
    def index(request):
        return render(request, 'jquery.html')

@csrf_exempt
def db_save(data):
    debug.log('db_save called')
    # DdaReuong_data = data
    # Dda_row = DdaReuong_data['rentBikeStatus']['row']
    # for objs in Dda_row:         
    #     _rackToint = objs['rackTotCnt']
    #     _stationName = objs['stationName']
    #     _parkingBikeToCnt = objs['parkingBikeTotCnt']
    #     _shared = objs['shared']
    #     _stationLatitude = objs['stationLatitude']
    #     _stationLongitude = objs['stationLongitude']
    #     _stationId = objs['stationId']

    #     to_Dda_db = dda_db(
    #     rackToint = _rackToint, 
    #     stationName = _stationName,
    #     parkingBikeToCnt = _parkingBikeToCnt,
    #     shared = _shared,
    #     stationLatitude = _stationLatitude,
    #     stationLongitude = _stationLongitude,
    #     stationId = _stationId)
    #     to_Dda_db.save()

@csrf_exempt
def db_select(data):
    db_conn = sqlite3.connect('./db.sqlite3')
    cursor = db_conn.cursor()
    query = ("Select stationName from DDA_DB where name LIKE %{0} ").format(data)
    cursor.execute(query)
