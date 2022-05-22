from django.urls import path
from .views import db_save

urlpatterns = [
   path('update_db/', db_save, name='db_save')
]