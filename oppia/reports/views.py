# oppia/reports/views.py

import datetime
import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from oppia.models import Course, Badge, Award, AwardCourse


from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from oppia.models import User, Course, Tracker, Activity
from oppia.profile.models import Province, District, Facility, UserProfile
from oppia.reports.forms import ProvinceDateDiffForm, DateDiffForm
from oppia.reports.permissions import *
from oppia.reports.signals import dashboard_accessed

def menu_reports(request):
    # add in here any reports that need to appear in the menu
    #return [{'name': 'test', 'url':'/reports/1/'},{'name': 'test2', 'url':'/reports/2/'}]

    if not reporting_access(request.user):
        return None
    
    return [
            { 'name': _(u'Unknown/Anonymous Users'),
              'url': reverse('oppia_report_incomplete_profiles')},
            { 'name': _(u'Pass/Failure Rates'),
              'url': reverse('oppia_report_pass_rate')},
            #{'name':_('Completion Rates'), 'url':reverse('oppia_completion_rates')}
            ]


def incomplete_profiles_view(request):
    # check user has report permissions
    if not reporting_access(request.user):
        return HttpResponse('Unauthorized', status=401)
    
    dashboard_accessed.send(sender=None, request=request, data=None)
    
    users = User.objects.filter(userprofile__location=None,is_staff=False)
    return render_to_response('oppia/reports/incomplete-profiles.html',
                              {'users': users,
                               }, 
                              context_instance=RequestContext(request))
  
'''
1. How many providers successfully completed the eLearning course in each Province by Course
type (e.g. ART), by district and by facility per quarter or year or specified period?
2. How many providers failed the eLearning course in each Province by Course type (e.g. ART), by
district and by facility per quarter or year or specified period?
'''  
def pass_rate_view(request):
    
    start_date = timezone.now() - datetime.timedelta(days=31)
    end_date = timezone.now()
    
    if request.method == 'POST':
        form = ProvinceDateDiffForm(request.POST)        
        form.fields['provinces'].choices = [(p.id,p.name) for p in reporting_province_access(request.user)]
        
        dashboard_accessed.send(sender=None, request=request, data=json.dumps(request.POST))
        
        if form.is_valid():
            start_date = form.cleaned_data.get("start_date")  
            start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
            end_date = form.cleaned_data.get("end_date")
            end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")      
            province = Province.objects.get(pk=form.cleaned_data.get("provinces"))
            
            courses = Course.objects.filter(is_draft=False,is_archived=False)
            districts = reporting_district_access(user=request.user,province=province).order_by('name')
            results = []
            
            for course in courses:
                result = {}
                result['course'] = course
                result['districts'] = []
                
                for district in districts:
                    district_results = {}
                    district_results['district'] = district
                    district_results['facilities'] = []
                    district_results['passed'] = 0
                    district_results['failed'] = 0
                    district_results['total'] = 0
                    
                    for i in range(1,int(settings.ISCHOOL_MAX_QUIZ_ATTEMPTS)+1):
                        district_results['passedattempt'+str(i)] = 0
                    
                    facilities = reporting_facility_access(user=request.user, district=district).order_by('name')
                    
                    for facility in facilities:
                        facility_results = {}
                        facility_results['facility'] = facility
                        for i in range(1,int(settings.ISCHOOL_MAX_QUIZ_ATTEMPTS)+1):
                            facility_results['passedattempt'+str(i)] = 0
                        
                        # get the quizzes for the course
                        quiz_acts = Activity.objects.filter(type=Activity.QUIZ,section__course=course).exclude(section__order=0).values_list('digest', flat=True)
                        trackers = Tracker.objects.filter(submitted_date__gte=start_date, submitted_date__lte=end_date,digest__in=quiz_acts, user__userprofile__location=facility)
                    
                        # get the total no people who passed/failed the quiz during this time
                        users_passed = []
                        users_failed = []
                        user_passed_attempts = {}
                        for i in range(1,int(settings.ISCHOOL_MAX_QUIZ_ATTEMPTS)+1):
                            user_passed_attempts['passedattempt'+str(i)] = []
                            
                        for counter, t in enumerate(trackers):
                            # check it's not more than the users 3rd attempt
                            no_previous_attempts = Tracker.objects.filter(submitted_date__lt=t.submitted_date,user=t.user,digest=t.digest).count()
                            if no_previous_attempts > (settings.ISCHOOL_MAX_QUIZ_ATTEMPTS-1):
                                continue
                            
                            if t.completed == True:
                                if t.user not in users_passed:
                                    users_passed.append(t.user)
                                    user_passed_attempts['passedattempt'+str(counter+1)].append(t.user)
                            else:
                                if t.user not in users_failed:
                                    users_failed.append(t.user)
            
                        users_failed = list(set(users_failed) - set(users_passed))
                                
                        facility_results['passed'] = users_passed
                        facility_results['failed'] = users_failed  
                        facility_results['total'] = len(users_failed) + len(users_passed)
                        
                        for i in range(1,int(settings.ISCHOOL_MAX_QUIZ_ATTEMPTS)+1):
                            facility_results['passedattempt'+str(i)] = set(user_passed_attempts['passedattempt'+str(i)])
                        
                 
                        district_results['passed'] += len(users_passed)
                        district_results['failed'] += len(users_failed)
                        district_results['total'] += len(users_failed) + len(users_passed)
                        
                        for i in range(1,int(settings.ISCHOOL_MAX_QUIZ_ATTEMPTS)+1):
                            district_results['passedattempt'+str(i)] += len(facility_results['passedattempt'+str(i)])
                        
                        district_results['facilities'].append(facility_results)
                        
                        
                    result['districts'].append(district_results)
                results.append(result)   
                
            return render_to_response('oppia/reports/pass-rate.html',
                                  {'results': results,
                                   'form': form,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   'province': province,
                                   }, 
                                  context_instance=RequestContext(request))
        return render_to_response('oppia/reports/pass-rate.html',
                                  {'form': form,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   }, 
                                  context_instance=RequestContext(request))
    else:
        data = {}
        data['start_date'] = start_date
        data['end_date'] = end_date
        form = ProvinceDateDiffForm(initial=data)
        form.fields['provinces'].choices = [(p.id,p.name) for p in reporting_province_access(request.user)]
        
        dashboard_accessed.send(sender=None, request=request, data=None)
        
        return render_to_response('oppia/reports/pass-rate.html',
                                  {'form': form,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   }, 
                                  context_instance=RequestContext(request))
     
     
'''
3. For any specified period, how many providers undertook the eLearning course?  How many failed to complete the course?
4. How many providers passed the eLearning course with a score of 80% or higher?
5. How many Providers attempted the Post Quiz once, twice or three times before passing the
course?
'''
        
def undertook_course_view(request):
       
    start_date = timezone.now() - datetime.timedelta(days=31)
    end_date = timezone.now()
    
    if request.method == 'POST':
        form = DateDiffForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get("start_date")  
            start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
            end_date = form.cleaned_data.get("end_date")
            end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")      
            
            courses = Course.objects.filter(is_draft=False,is_archived=False)
            results = []
            
            for course in courses:
               pass
                
            return render_to_response('oppia/reports/undertook-course.html',
                                  {'results': results,
                                   'form': form,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   }, 
                                  context_instance=RequestContext(request))
        return render_to_response('oppia/reports/undertook-course.html',
                                  {'form': form,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   }, 
                                  context_instance=RequestContext(request))
    else:
        data = {}
        data['start_date'] = start_date
        data['end_date'] = end_date
        form = DateDiffForm(initial=data)
        
        return render_to_response('oppia/reports/undertook-course.html',
                                  {'form': form,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   }, 
                                  context_instance=RequestContext(request)) 
    
    
def completion_rates(request):

    courses, response = can_view_courses_list(request)
    if response is not None:
        return response

    courses_list = []
    for course in courses:
        obj = {}
        obj['course'] = course

        courseActivities = course.get_no_activities()
        no_users = User.objects.filter(tracker__course=course).distinct().count()

        awards_given = AwardCourse.objects.filter(course=course).count()

        obj['enroled'] = no_users
        if no_users > 0:
            obj['completion'] = (float(awards_given) / float(no_users)) * 100
        else:
            obj['completion'] = 0
            
        courses_list.append(obj)

    return render_to_response('oppia/reports/completion_rates.html',
                              {'courses_list': courses_list },
                              context_instance=RequestContext(request))

def course_completion_rates(request,course_id):

    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)

    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404

    users_completed = []
    users_incompleted = []

    courseActivities = course.get_no_activities()
    users = User.objects.filter(tracker__course=course).distinct()
    for user in users:
        userActivities = Course.get_activities_completed(course, user)
        userObj = {'user': user}
        userObj['activities_completed'] = userActivities
        userObj['completion_percent'] = (userActivities * 100 / courseActivities)
        if (userActivities >= courseActivities):
            users_completed.append(userObj)
        else:
            users_incompleted.append(userObj)

    return render_to_response('oppia/reports/course_completion_rates.html',
                              {
                                  'course': course,
                                  'users_enroled_count': len(users_completed) + len(users_incompleted),
                                  'users_completed': users_completed,
                                  'users_incompleted': users_incompleted,
                              },
                              context_instance=RequestContext(request))

def can_view_courses_list(request):
    if not request.user.is_staff:
        return None, HttpResponse('Unauthorized', status=401)
    else:
        courses = Course.objects.filter(is_draft=False,is_archived=False).order_by('title')
    return courses, None

