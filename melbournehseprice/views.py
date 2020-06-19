from django.views.generic import (ListView, DetailView,
 CreateView, DeleteView, UpdateView)
from django.views.generic import TemplateView
from melbournehseprice.models import House, Location
from django.urls import reverse_lazy


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


class CreateHouse(CreateView):
    model = House
    fields = '__all__'
    template_name_suffix = '_form'
    
class UpdateHouse(UpdateView):

    model = House
    
    fields = '__all__'
    
    template_name_suffix = '_form'
    
    success_url = reverse_lazy('houselist')
    

class HouseDelete(DeleteView):
    model = House
    
    success_url = reverse_lazy('houselist')
    

class CreateLocation(CreateView):
    model = Location
    fields = '__all__'
    template_name_suffix = '_form'


class UpdateLocation(UpdateView):

    model = Location
    
    fields = '__all__'
    
    template_name_suffix = '_form'
    
    success_url = reverse_lazy('locationlist')
    
    
class LocationDelete(DeleteView):
    model = Location
    
    success_url = reverse_lazy('locationlist')
    
