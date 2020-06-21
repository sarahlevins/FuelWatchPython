from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'fuelwatch'

urlpatterns = [
    path('', views.index, name='index'),
    path('getfuel/', views.getfuel),
    path('getfuelprices/', views.getfuelprices)
]
