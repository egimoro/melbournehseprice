from django.urls import path
from melbournehseprice.views import (HouseList, IndexView, LocationList, 
                                     HouseDetail, LocationDetail,
                                     CreateHouse, UpdateHouse, HouseDelete,
                                     CreateLocation, UpdateLocation, LocationDelete)




urlpatterns = [ path('', IndexView.as_view(), name='index'),  
                path('melbournehseprice/houselist/', HouseList.as_view(),
                     name='houselist'),
                path('melbournehseprice/locationlist', LocationList.as_view(),
                     name='locationlist'),
                path('melbournehseprice/housedetail/<int:pk>', 
                      HouseDetail.as_view(), name='housedetail'),
                path('melbournehseprice/locationdetail/<int:pk>',
                      LocationDetail.as_view(), name='locationdetail'),
                path('melbournehseprice/house_create', CreateHouse.as_view(),
                     name='house_create'),
                path('melbournehseprice/house_update/<int:pk>', UpdateHouse.as_view(),
                     name='house_update'),
                path('melbournehseprice/house_delete/<int:pk>', HouseDelete.as_view(),
                      name='house_delete'),
                path('melbournehseprice/location_create', CreateLocation.as_view(),
                     name='location_create'),
                path('melbournehseprice/location_update/<int:pk>', UpdateLocation.as_view(),
                     name='location_update'),
                path('melbournehseprice/location_delete/<int:pk>', LocationDelete.as_view(),
                       name='location_delete'),]
                
