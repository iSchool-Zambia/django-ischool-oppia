# oppia/reports/admin.py
from django.contrib import admin

from oppia.reports.models import ReportingPermissions

class ReportingPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'province', 'district', 'facility')
    
    
admin.site.register(ReportingPermissions, ReportingPermissionsAdmin)   