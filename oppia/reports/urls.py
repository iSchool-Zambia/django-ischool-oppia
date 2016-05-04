# oppia/reports/urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^incomplete-profiles/$', 'oppia.reports.views.incomplete_profiles_view', name="oppia_report_incomplete_profiles"),  
    url(r'^pass-rate-by-course/$', 'oppia.reports.views.pass_rate_view_by_course', name="oppia_report_pass_rate_by_course"),    
    url(r'^pass-rate-all-courses/$', 'oppia.reports.views.pass_rate_view_all_courses', name="oppia_report_pass_rate_all_courses"),     
    url(r'^undertook-course/$', 'oppia.reports.views.undertook_course_view', name="oppia_report_undertook_course"),     
    url(r'^completion_rates/$', 'oppia.reports.views.completion_rates', name="oppia_completion_rates"),
    url(r'^completion_rates/(?P<course_id>\d+)/$', 'oppia.reports.views.course_completion_rates', name="course_completion_rates"),
    )
