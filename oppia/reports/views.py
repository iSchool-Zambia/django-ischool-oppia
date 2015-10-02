# oppia/reports/views.py
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from oppia.models import User, UserProfile

def menu_reports(request):
    # add in here any reports that need to appear in the menu
    #return [{'name': 'test', 'url':'/reports/1/'},{'name': 'test2', 'url':'/reports/2/'}]
    return [
            { 'name': _(u'Incomplete Profiles'),
              'url': reverse('oppia_report_incomplete_profiles')}
            ]


def incomplete_profiles_view(request):
    users = User.objects.filter(userprofile__facility=None,is_staff=False)
    return render_to_response('oppia/reports/incomplete-profiles.html',
                              {'users': users,
                               }, 
                              context_instance=RequestContext(request))