# oppia/profile/admin.py

from django.contrib import admin

from oppia.profile.models import Province, District, Facility, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'can_upload', 'about', 'job_title', 'organisation')
    
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name'] 
    
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ['name'] 

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'code', 'type', 'active') 
    search_fields = ['name','type','code'] 
    
admin.site.register(Province, ProvinceAdmin)  
admin.site.register(District, DistrictAdmin) 
admin.site.register(Facility, FacilityAdmin) 
admin.site.register(UserProfile, UserProfileAdmin)

