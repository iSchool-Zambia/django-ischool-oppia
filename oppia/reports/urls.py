# oppia/reports/urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
           
    url(r'^incomplete-profiles/$', 'oppia.reports.views.incomplete_profiles_view', name="oppia_report_incomplete_profiles"),  
    url(r'^pass-rate/$', 'oppia.reports.views.pass_rate_view', name="oppia_report_pass_rate"),      
    url(r'^undertook-course/$', 'oppia.reports.views.undertook_course_view', name="oppia_report_undertook_course"),     
                       
    )
