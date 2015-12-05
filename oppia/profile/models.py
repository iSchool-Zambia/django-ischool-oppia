from django.db import models
from django.utils.translation import ugettext_lazy as _

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
    
    class Meta:
        verbose_name = _('Facility')
        verbose_name_plural = _('facilities')
        
    def __unicode__(self):
        return self.name