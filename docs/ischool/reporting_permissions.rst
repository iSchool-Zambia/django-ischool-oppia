Permissions for Report Access
==============================

A custom permissions system is set up to allow users to be given specific permissions to the reports, 
at a province, district and facility level.

To grant a specific user access to the reports for specific facilities, districts or provinces, and administrator will need to:

* Go to the Django Admin pages (either from the server dashboard menu bar, or directly at: http://ischool.oppia-mobile.org/admin)
* Click on the 'Reporting Permissions' link in the list of data models
* Click on 'Add reporting permission'
* Select the user from the drop down list
* **Either** select a province, district or facility. Selecting a particular province will then automatically give access to all the districts and facilities in that province. 
  Similarly, if a district is selected, permissions for all the facilities in that district will be given.

Notes:
-------

* Django admin and staff users automatically have access to all the reports and provinces, districts and facilities.
* Multiple permissions may be given to any user, so, for example, to a specific set of facilities (even if not within the same district or province)
* Only facilities flagged as 'active' will appear in any reports (see: :doc:`facilities` for setting the 'active' status)
* All users attached to a specific facility will be included in the reporting


Example Scenarios:
---------------------

**Staff in provincial health office**: 
Staff in the health office/bureau for Province A requiring access to all the facilities in that Province. In this case assign the user to Province A in the reporting permissions.


**District health manager**: 
Management staff in the District B health office requiring access to all the facilities in that district. In this case assign the user to District A in the reporting permissions.


**Facilities supervisor**: 
A facilities supervisor requiring access for a specific set of facilities, but not the whole district. In this case assign the user to each facility they are responsible for.

**Facility manager**: 
A facility manager requiring access just for the facility they manage. In this case assign the user just to the one specific facility.