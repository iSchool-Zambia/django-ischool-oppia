

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from oppia.profile.models import Province, District, Facility
 
class ReportingPermissions (models.Model):
    user = models.ForeignKey(User)
    province = models.ForeignKey(Province,null=True, blank=True, default=None)
    district = models.ForeignKey(District,null=True, blank=True, default=None)
    facility = models.ForeignKey(Facility,null=True, blank=True, default=None)