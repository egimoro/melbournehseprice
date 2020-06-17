from django.urls import path
from melbournehseprice.views import (HouseList, IndexView, LocationList, 
                                     HouseDetail, LocationDetail)




urlpatterns = [ path('', IndexView.as_view(), name='index'),  
                path('melbournehseprice/houselist/', HouseList.as_view(),
                     name='houselist'),
                path('melbournehseprice/locationlist', LocationList.as_view(),
                     name='locationlist'),
                path('melbournehseprice/housedetail/<int:pk>', 
                      HouseDetail.as_view(), name='housedetail'),
                path('melbournehseprice/locationdetail/<int:pk>',
                      LocationDetail.as_view(), name='locationdetail'),]
