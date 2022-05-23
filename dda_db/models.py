from django.db import models

# Create your models here.
class dda_db(models.Model):
    rackTotCnt = models.IntegerField() # ID?
    stationName = models.CharField(max_length= 32) # 대여소 이름
    parkingBikeToCnt = models.IntegerField() # 대여소에 남아있는 자전거 수
    shared = models.IntegerField() # 빌려간 수
    stationLatitude = models.FloatField() # Lat
    stationLongitude = models.FloatField() # Long
    stationId = models.CharField(max_length= 32) 

    class Meta():
        db_table = 'DDA_DB'