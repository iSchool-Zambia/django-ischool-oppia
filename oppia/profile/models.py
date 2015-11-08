from django.db import models

class Province (models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    
class District (models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=200, blank=False, null=False)

class Facility (models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=200, blank=False, null=False)