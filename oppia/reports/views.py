# oppia/reports/views.py
import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from oppia.models import User, UserProfile, Course, Tracker, Activity
from oppia.profile.models import Province, District, Facility
from oppia.reports.forms import ProvinceDateDiffForm, DateDiffForm

def menu_reports(request):
    # add in here any reports that need to appear in the menu
    #return [{'name': 'test', 'url':'/reports/1/'},{'name': 'test2', 'url':'/reports/2/'}]
    return [
            { 'name': _(u'Incomplete Profiles'),
              'url': reverse('oppia_report_incomplete_profiles')},
            { 'name': _(u'Pass/Failure Rates'),
              'url': reverse('oppia_report_pass_rate')}
            ]


def incomplete_profiles_view(request):
    users = User.objects.filter(userprofile__facility=None,is_staff=False)
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
    results = []
    if request.method == 'POST':
        form = ProvinceDateDiffForm(request.POST)
        form.fields['provinces'].choices = [(p.id,p.name) for p in Province.objects.all()]
        if form.is_valid():
            start_date = form.cleaned_data.get("start_date")  
            start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
            end_date = form.cleaned_data.get("end_date")
            end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")      
            province = Province.objects.get(pk=form.cleaned_data.get("provinces"))
            
            results_title = ("Pass/Fail for province '%s' between '%s' and '%s' " % (province.name, start_date, end_date))
            
            courses = Course.objects.filter(is_draft=False,is_archived=False)
            
            for course in courses:
                result = {}
                result['course'] = course
                
                # get the quizzes for the course
                quiz_acts = Activity.objects.filter(type=Activity.QUIZ,section__course=course).exclude(section__order=0).values_list('digest', flat=True)
                trackers = Tracker.objects.filter(submitted_date__gte=start_date, submitted_date__lte=end_date,digest__in=quiz_acts)
            
                # get the total no people who passed/failed the quiz during this time
                users_passed = []
                users_failed = []
                for t in trackers:
                    # check it's not more than the users 3rd attempt
                    no_previous_attempts = Tracker.objects.filter(submitted_date__lt=t.submitted_date,user=t.user,digest=t.digest).count()
                    if no_previous_attempts > 2:
                        continue
                    
                    if t.completed == True:
                        users_passed.append(t.user)
                    else:
                        users_failed.append(t.user)
    
                users_failed = list(set(users_failed) - set(users_passed))
                        
                result['passed'] = users_passed
                result['failed'] = users_failed    
                 
                results.append(result)   
    
    else:
        data = {}
        data['start_date'] = start_date
        data['end_date'] = end_date
        form = ProvinceDateDiffForm(initial=data)
        form.fields['provinces'].choices = [(p.id,p.name) for p in Province.objects.all()]
        results_title = None
        
    
    
    return render_to_response('oppia/reports/pass-rate.html',
                              {'results': results,
                               'form': form,
                               'start_date': start_date,
                               'end_date': end_date,
                               'results_title': results_title,
                               }, 
                              context_instance=RequestContext(request))
     
     
'''
3. For any specified period, how many providers undertook the eLearning course?  How many failed to complete the course?
'''
    
    
'''
4. How many providers passed the eLearning course with a score of 80% or higher?
'''

'''
5. How many Providers attempted the Post Quiz once, twice or three times before passing the
course?
'''
