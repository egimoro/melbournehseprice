from django.db import models
from datetime import datetime

class House(models.Model):
    rooms = models.IntegerField(default=0)
    hsetype = models.CharField(max_length=1)
    price = models.FloatField(default=0)
    method = models.CharField(max_length=3)
    datesold = models.DateField() 
    
    def __str__(self):
        return self.hsetype
    

class Location(models.Model):
    suburb = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    postcode = models.CharField(max_length=4)
    property_count = models.IntegerField(default=0)
    distance = models.FloatField(default=0)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.suburb
        
    
    

    
    
    

    
    
    
 
    
    

    


