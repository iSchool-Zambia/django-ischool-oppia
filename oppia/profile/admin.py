# oppia/profile/admin.py
from django.contrib import admin

from oppia.profile.models import Province, District, Facility

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name'] 
    
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name'] 

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ['name'] 
    
admin.site.register(Province, ProvinceAdmin)  
admin.site.register(District, DistrictAdmin) 
admin.site.register(Facility, FacilityAdmin) 