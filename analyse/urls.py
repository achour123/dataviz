from django.urls import path
from django.conf.urls import url

from . import views

app_name='analyse'
urlpatterns = [
    path('', views.analy,name='analy'),    
]

