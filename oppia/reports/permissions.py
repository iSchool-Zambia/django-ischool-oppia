# oppia/reports/permissions.py

from django.contrib.auth.models import User

from itertools import chain

from oppia.reports.models import ReportingPermissions
from oppia.profile.models import Province, District, Facility

# Can access reports at allb
def reporting_access(user): 
    if user.is_staff:
        return True
    
    specific_permission = ReportingPermissions.objects.filter(user=user)
    
    if specific_permission.count() > 0:
        return True
    else:
        return False

# which facilities can user access
def reporting_facility_access(user):
    if not reporting_access(user):
        return None
    
    if user.is_staff:
        # get all the active facilities
        return Facility.objects.filter(active=True)
      
    # check the province specific access
    provinces = Facility.objects.filter(active=True, district__province__reportingpermissions__user=user).distinct()
    
    # check the district specific access
    districts = Facility.objects.filter(active=True, district__reportingpermissions__user=user).distinct()
    
    # check the facility specific access
    facilities = Facility.objects.filter(active=True, reportingpermissions__user=user).distinct()
    
    all_facilities = set(chain(provinces, districts, facilities))
    
    return all_facilities

# which districts can user access
def reporting_district_access(user):
    if not reporting_access(user):
        return None
    
    if user.is_staff:
        # get all the active facilities
        return District.objects.filter(facility__active=True).distinct()
    
     # check the province specific access
    provinces = District.objects.filter(facility__active=True, province__reportingpermissions__user=user).distinct()
    
    # check the district specific access
    districts = District.objects.filter(facility__active=True, reportingpermissions__user=user).distinct()
    
    # check the facility specific access
    facilities = District.objects.filter(facility__active=True, facility__reportingpermissions__user=user).distinct()
    
    all_districts = set(chain(provinces, districts, facilities))
    
    return all_districts

# which provinces can user access
def reporting_province_access(user):
    if not reporting_access(user):
        return None
    
    if user.is_staff:
        # get all the active facilities
        return Province.objects.filter(district__facility__active=True).distinct()
    
     # check the province specific access
    provinces = Province.objects.filter(district__facility__active=True, reportingpermissions__user=user).distinct()
    
    # check the district specific access
    districts = Province.objects.filter(district__facility__active=True, district__reportingpermissions__user=user).distinct()
    
    # check the facility specific access
    facilities = Province.objects.filter(district__facility__active=True, district__facility__reportingpermissions__user=user).distinct()
    
    all_provinces = set(chain(provinces, districts, facilities))
    
    return all_provinces

# which users can user access
def reporting_user_access(user):
    if not reporting_access(user):
        return None
    
    if user.is_staff:
        # get all the active facilities
        return User.objects.filter(userprofile__location__active=True).distinct()
    
    facilities = reporting_facility_access(user)

    return User.objects.filter(userprofile__location__in=facilities)