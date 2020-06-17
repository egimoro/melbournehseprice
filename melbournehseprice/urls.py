from django.urls import path
from melbournehseprice.views import HouseList, IndexView, LocationList




urlpatterns = [ path('', IndexView.as_view(), name='index'),  
                path('melbournehseprice/houselist/', HouseList.as_view(),
                     name='houselist'),
                path('melbournehseprice/locationlist', LocationList.as_view(),
                     name='locationlist'),]
