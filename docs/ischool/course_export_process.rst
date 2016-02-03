iSchool Course Export Process
==================================

Basic instructions for updating and the pushing a course to the iSchool Oppia server:


#. Log into Moodle (http://moodle.digital-campus.org) and go to the Ischool Zambia area (http://moodle.digital-campus.org/course/index.php?categoryid=30)
#. Either go into the course where you'd like to add the content, or create a new course
#. Once in the course homepage click the "turn editing on" button (in top right of banner bar)
#. Select "add an activity or resource" in the relevant topic/section (these can be moved around afterwards if needed)
#. From the pop up window select the 'page' option (very near the bottom of the list)
#. On the editing page enter a page title and description in the relevant fields. The description isn't actually displayed in the app, unless an image is uploaded - in which case the image is used as the icon for the activity in the app.
#. In the 'page content' field, you'll need to switch to the html view - click on the 'show more buttons' icon on the far left, then in the new row that appears click the 'HTML' button on the far right.
#. Enter the iframe HTML, with the full localhost url that you'll be using on the phone
#. Press "save and return to course"
#. Once you've added all the activities needed, from the course homepage, go to the 'Oppia Mobile Export' block on the right hand column and press the 'Export to Oppia Package' button
#. On the step 1 page, you can set a 'course priority' - this is if you'd like the courses to appear in a specific order in the app, instead of alphabetical by the course title. The "course tags" are used to classify the course when downloading in the app - at least one tag should be entered, else it won't display in the app course download page.
#. Press continue, it'll now generate the course zip package
#. On the resulting page, you can either download the course zip package directly (eg if you want to manually test/install on the tablet), or you can directly publish to the Oppia server
#. For publishing directly you'll need to enter your username and password for the Oppia server, and you have another change to edit the tags. The "is draft" option means that, if ticked, only admins will see it displayed in the app (useful for testing during course development until you want the course available for everyone)
#. Once successfully published you can open up the app on your device, from the main app page, go to the menu and select 'download courses', then you can select the tag(s) that you published the course under, then it'll list the courses under that tag and the option to download/update.
#. Once downloaded/updated it's ready to view on the device

Notes & Comments:


* Each topic will need a specific summary (used in the app as the topic/section title), so under the 'topic 1' or whatever title, click the 'edit summary' cog icon and enter the name in the summary box. If the topic doesn't have a summary it'll be ignored on export
* For creating quizzes generally it's the same process, except at step 5 above, you'd select 'quiz' instead
* For pre-test quizzes, these should be in the very top section of the Moodle course ("topic 0")  - in Oppia, the users will then have to complete a quiz that's here before they can view the rest of the course content

