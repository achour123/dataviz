from django.urls import path

from . import views


app_name='formulaire'

urlpatterns = [
    path('', views.formul, name='formul'),
   
]