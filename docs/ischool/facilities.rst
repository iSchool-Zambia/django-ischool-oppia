Provinces, Districts and Facilities
======================================

All the provinces, districts and facilities for Zambia are pre-loaded into the server. However 
since there are a large number and this project is currently only working with a select few facilities,
each facility in the database has an 'active' flag.

The 'active' flag determines whether the facility (and hence parent district and province) will appear
in the reporting - only the facilities with the 'active' flag set to true will appear in the reports 
(and therefore also only those health workers attached to the active facilities).

To make a facility active or not, an administrator will need to update this:

* Go to the Django Admin pages (either from the server dashboard menu bar, or directly at: http://ischool.oppia-mobile.org/admin)
* Click on the 'Facilities' link is the list of data models
* Browse or search for the particular facility and click to edit
* Tick or untick the 'active' field and click the save button