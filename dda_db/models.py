from django.db import models

# Create your models here.
class dda_db(models.Model):
    rackTotCnt = models.IntegerField() # 대여소ID
    stationName = models.CharField(max_length= 64) # 대여소 이름
    parkingBikeToCnt = models.IntegerField() # 자전거주차총건수
    shared = models.IntegerField() # 거치율
    stationLatitude = models.FloatField() # 위도
    stationLongitude = models.FloatField() # 경도
    stationId = models.CharField(max_length= 32) #대여소ID

    class Meta():
        db_table = 'DDA_DB'