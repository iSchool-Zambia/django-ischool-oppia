# oppia/reports/models.py


from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

from oppia.profile.models import Province, District, Facility
 
class ReportingPermissions (models.Model):
    user = models.ForeignKey(User)
    province = models.ForeignKey(Province,null=True, blank=True, default=None)
    district = models.ForeignKey(District,null=True, blank=True, default=None)
    facility = models.ForeignKey(Facility,null=True, blank=True, default=None)


class DashboardAccessLog (models.Model):
    user = models.ForeignKey(User,null=True, blank=True, default=None, on_delete=models.SET_NULL)
    access_date = models.DateTimeField('date created',default=timezone.now)
    ip = models.GenericIPAddressField(blank=True, null=True, default=None)
    agent = models.TextField(blank=True, null=True, default=None)
    url = models.TextField(blank=True, null=True, default=None)
    data = models.TextField(blank=True, null=True, default=None)
    