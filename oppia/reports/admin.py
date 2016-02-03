# oppia/reports/admin.py

from django.contrib import admin

from oppia.reports.models import ReportingPermissions, DashboardAccessLog

class ReportingPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'province', 'district', 'facility')

class DashboardAccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'access_date', 'url', 'ip')
    
admin.site.register(DashboardAccessLog, DashboardAccessLogAdmin) 
admin.site.register(ReportingPermissions, ReportingPermissionsAdmin) 

