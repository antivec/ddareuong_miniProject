"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from dda_db.models import dda_db




urlpatterns = [
    path('admin/', admin.site.urls),
    path('dda_db/',include('dda_db.urls')), ## 관리자용 DB관리 페이지
    path('',include('bikeapp.urls')), ## BIKEAPP 24일 아침 버전일거에요~ // 저녁까지 진행된 bikeapp 갱신 필요
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = +[
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]