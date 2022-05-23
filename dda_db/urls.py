from django.urls import path
from .views import MainpageView
from . import views as dda_view

app_name = 'dda_db'

urlpatterns = [
   path('', MainpageView.as_view(), name='mainPage'),
   path('db_save/',dda_view.db_save, name='db_save'),
   path('db_select/',dda_view.db_select,name='db_select')
]