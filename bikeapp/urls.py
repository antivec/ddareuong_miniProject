from django.urls import path
from. import views
from .views import *

app_name = 'bikeapp'

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('mapfind/', views.findmap) ,
    path('mapfind/result/',views.result),
    path('mapfind/result/directions/', views.directions),
    
]
