from distutils.log import debug
from django.shortcuts import render
from dda_db.models import dda_db
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import json
import requests as req


@csrf_exempt
def db_save(data):
    debug.log("!")
    DdaReuong_data = data
    Dda_row = DdaReuong_data['rentBikeStatus']['row']
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
        to_Dda_db.save()

def db_select(data):
    db_conn = sqlite3.connect('./db.sqlite3')
    cursor = db_conn.cursor()
    query = ("Select stationName from DDA_DB where name LIKE {0} ").format(data)
    cursor.execute(query)
