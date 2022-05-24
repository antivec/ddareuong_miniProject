from django.urls import path
from .views import MainpageView
from . import views as dda_view

app_name = 'dda_db'

urlpatterns = [
   path('', MainpageView.as_view(), name='mainPage'),
   path('db_save_1_to_1000/',dda_view.db_save_1_to_1000, name='db_save_1_to_1000'),
   path('db_save_remaining/',dda_view.db_save_remaining, name='db_save_remaining'),
   path('db_select/',dda_view.db_select_LatLong,name='db_select_LatLong')
]