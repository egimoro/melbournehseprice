from django.contrib import admin

from .models import House, Location

class HouseAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['rooms', 'hsetype', 'price', 'method', 'datesold']})]
   
admin.site.register(House, HouseAdmin)   
admin.site.register(Location)       



