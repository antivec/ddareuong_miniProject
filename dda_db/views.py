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
        return render(request, 'jquery.html')\

def db_insert(objs):
    to_Dda_db = dda_db(
    rackTotCnt = objs['rackTotCnt'],
    stationName = objs['stationName'],
    parkingBikeToCnt = objs['parkingBikeTotCnt'],
    shared = objs['shared'],
    stationLatitude = objs['stationLatitude'],
    stationLongitude = objs['stationLatitude'],
    stationId = objs['stationLatitude'])            
    to_Dda_db.save()
    return 

def db_update(objs):
    update_date = dda_db.objects.get(stationName = objs['stationName']) #이미 있는 대여소의 데이터를 갱신할때
    update_date.rackTotCnt = objs['rackTotCnt']
    update_date.parkingBikeToCnt = objs['parkingBikeTotCnt']
    update_date.shared = objs['shared']
    update_date.stationLatitude = objs['stationLatitude']
    update_date.stationLongitude = objs['stationLatitude']
    update_date.stationId = objs['stationLatitude']
    update_date.save()
    return

#####################################주의#####################################################
##호출시 시스템 부하로 한번에 최대 1,000건를 초과할수 없습니다.                                  #
##2회 나누어 호출하시기 바랍니다. 예) 1/1,000, 1001/2,000 (대여소 수 : '18.11월말기준 1,471개소) #
##############################################################################################
@csrf_exempt
def db_save_1_to_1000(request):
    url = "http://openapi.seoul.go.kr:8088/4f4557774d776f6431323044696f6a77/json/bikeList/1/1000"  #1에서 1000개 index 요청
    result = "DB Updated!!" # default result string --> DB 갱신 알림
    if request.method == 'POST':
        try:
            my_req = Request(url)
            my_req.get_method = lambda : 'GET'
            data = urlopen(my_req).read()
            Dda_row = json.loads(data)['rentBikeStatus']['row']
            
            for objs in Dda_row:      
                if dda_db.objects.filter(stationName = objs['stationName']).exists() == False:  #db에 새로운 따릉이 대여소가 생겼을때     
                    db_insert(objs)
                else:
                    db_update(objs)

        except Exception as e: #에러 발생시 브라우저에 alert 표시
            result = "Error Occured !! ({0})".format(e)
    return HttpResponse(result)

@csrf_exempt
def db_select(data):
    db_conn = sqlite3.connect('./db.sqlite3')
    cursor = db_conn.cursor()
    query = ("Select stationName from DDA_DB where name LIKE %{0} ").format(data)
    cursor.execute(query)
