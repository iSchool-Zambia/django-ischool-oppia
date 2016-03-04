# oppia/profile/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from oppia.models import Participant


class Province (models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    
    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')
        
    def __unicode__(self):
        return self.name
    
class District (models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=200, blank=False, null=False)
    
    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')
        
    def __unicode__(self):
        return self.name
    

class Facility (models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=200, blank=False, null=False)
    code = models.CharField(max_length=50, blank=True, null=False, default="")
    active = models.BooleanField(blank=False, null=False, default=True)
    type = models.CharField(max_length=200, blank=True, null=False, default="")
    
    class Meta:
        verbose_name = _('Facility')
        verbose_name_plural = _('facilities')
        
    def __unicode__(self):
        return self.name
    
    def get_name_full(self):
        return self.district.province.name + " > " + self.district.name + " > " + self.name

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    about = models.TextField(blank=True, null=True, default=None)
    can_upload = models.BooleanField(default=False)
    job_title = models.TextField(blank=True, null=True, default=None)
    organisation = models.TextField(blank=True, null=True, default=None)
    phone_number = models.TextField(blank=True, null=True, default=None)
    # ischool specific starts
    profession = models.TextField(blank=True, null=True, default=None)
    years_in_service = models.TextField(blank=True, null=True, default=None)
    location = models.ForeignKey(Facility, null=True, blank=True, default=None, on_delete=models.SET_NULL) 
    # ischool specific ends

    def get_can_upload(self):
        if self.user.is_staff:
            return True
        return self.can_upload

    def is_student_only(self):
        if self.user.is_staff:
            return False
        teach = Participant.objects.filter(user=self.user,role=Participant.TEACHER).count()
        if teach > 0:
            return False
        else:
            return True

    def is_teacher_only(self):
        if self.user.is_staff:
            return False
        teach = Participant.objects.filter(user=self.user,role=Participant.TEACHER).count()
        if teach > 0:
            return True
        else:
            return False

