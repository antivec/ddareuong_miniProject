from django.urls import path
from .views import MainpageView

app_name = 'dda_db'

urlpatterns = [
   path('', MainpageView.as_view(), name='mainPage')
]