from django.urls import path

from .views import *


urlpatterns = [
    path('',link),
    path('index/',index,name='index'),
    path('zyc/',zyc,name='zyc')
]