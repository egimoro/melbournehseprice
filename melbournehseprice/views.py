from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from melbournehseprice.models import House, Location


class IndexView(TemplateView):
    
    template_name = 'melbournehseprice/index.html'

    

    

class HouseList(ListView):
    
    
    context_object_name = 'house_list'  
    template_name = 'melbournehseprice/houselist.html'
    queryset = House.objects.all()


class LocationList(ListView):
    
    context_object_name = 'location_list'
    template_name =  'melbournehseprice/locationlist.html'
    queryset = Location.objects.all()


class HouseDetail(DetailView):
    model = House
    template_name = 'melbournehseprice/housedetail.html'
    

class LocationDetail(DetailView):
    model = Location
    template_name = 'melbournehseprice/locationdetail.html'



