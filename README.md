# Your Poetry　のAPI

詩をシェアするウェブアプリ「Your Poetry」のAPI
Django Rest Frameworkを使用しました。

Your Poetry:
https://github.com/rkyzk/poetry-2023

---
# Django Rest Framework API for 'Your Poetry' project

## Contents 
* [Overview](#overview)
* [Main Technologies Used](#main-technologies-used)
* [Features](#features-in-nutshell)
* [Manual Testing](#manual-testing)
* [Testing Code](#testing-code)
* [Deployment Process](#deployment-process)
* [Credits](#credits)

## Overview
This Django Rest Framework API serves as the backend for "Your Poetry" application -- a platform for sharing poetry.
The API contains apps that handle data about poems, user profiles, comments on the poems as well as which users liked which poems (likes app) and which users follows which users (followers app.)

The app can be found [here](https://poetry-6c31c94e3988.herokuapp.com/)

## Main Technologies
Django Rest Framework

### Features
This API contains the following six apps. 

1. poems<br>
- Logged in users can create a poem by entering the title, content (required fields) and select a category (‘other’ by default), and the data will be handled by poems app.
- The owner of the poem can edit or delete it.

2. profiles<br>
- A profile object will be automatically created when a new user object is made.  This is done by def create_profile method in the models.py module.
- Users can enter display name, an introduction about themselves (field 'about_me'), their favorite poems and poets (field 'favorites') and upload an image.

3. comments<br>
- Comments can be written, edited or deleted by logged in users.
- Comment model has a foreign key 'poem' which keeps track on which poem the comment has been written about.
- Only the owner of the comments can edit or delete the comments.

4. likes<br>
- ‘Like’ object will be created when a user likes a poem. 
- 'unique_together' defined in the Meta class in the Like model makes sure that a user can’t like the same poem twice.

5. followers<br>
- ‘Follower’ object will be created when a user follows a user.
- 'unique_together' makes sure that a user can’t follow a user twice.

**Other features**<br>
*permissions class*<br>
- IsOwnerOrReadOnly will examine if the user is the owner of an object, and if so, returns true.  This will be used to programtaically prevent users other than the owner of the object from accessing the editing and deleting functionalities of the object.

*dj-rest-auth bug fix*<br>
- Due to a bug in dj-rest-auth, users cannot log out.  The reason is that even though the samesite attribute is set to “None” in settings.py, this is not passed to the log out view.
- As a solution to this bug, a method def logout_route is written in rest-framework_api/views.py (this was taken from the DRF walk through project at CI).  As explained in the lesson ‘dj-rest-auth bug fix’ at CI,
this method sets both cookies to an empty string and pass additional attributes such as secure, httponly and samesite, which were left out by mistake by the library.

## Manual Testing

I made changes to this app over time, and the manual testing needs to be reconducted. (Oct. 15th, 2023)

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|message at root | Go to root URL "https://poetry-6c31c94e3988.herokuapp.com" | Check the displayed information | Message "Welcome to my drf API!" is displayed. |message "Welcome to my drf API!" is displayed.| pass|[image](./images/manual-tests/DRF/1.png)|2023/8/8|

### Profiles

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|A profile is automatically made for a new user.|Go to admin panel, add user (username:'user1' password: 'swUf8LcR'.)|Go to "/profiles" and check if User object 'user1' is created. |'user1' is created.|'user1' is created.| pass|[image](./images/manual-tests/DRF-profiles/1&2.png)|2023/7/29|
|2|'sunset.jpg' is set as default profile image. |--| Go to "/profiles" and check if the value of 'image' for user1 is "https://res.cloudinary.com/ds66fig3o/image/upload/v1/media/../sunset.jpg". | The correct URL is set for 'image' field. |The correct URL is set for 'image' field.| pass|[image](./images/manual-tests/DRF-profiles/1&2.png)|2023/7/29|
|3|profile can be edited if logged in and owner. |log in as admin| Go to "/profiles/1" (1 is admin's id) and update the data as follows: display name: admin display name; about me: Im admin; favorites: my favorites. Click 'PUT.' |The data are updated. |The data are updated.| pass|[image](./images/manual-tests/DRF-profiles/4.png)|2023/7/29|
|4|profile image can be updated. || Go to "/profiles/1" and upload 'test-profile.jpg' Click 'PUT.' |The image URL is updated and contains 'test-profile'. |The image URL is updated. The URL shows 'test-profile.jpg'. | pass|[image1 ](./images/manual-tests/DRF-profiles/4-1.png)[image](./images/manual-tests/DRF-profiles/4-2.png)|2023/7/29|
|5|file size validation||Upload ‘image-over-800KB.jpeg, which is 822KB in size.|A validation message will say "Files larger than 800KB can't be uploaded."| A validation message will say "Files larger than 800KB can't be uploaded."|pass|[image1 ](./images/manual-tests/DRF-profiles/5-1.png)[image2](./images/manual-tests/DRF-profiles/5-2.png)|2023/8/5|
|6|file height validation||Upload ‘image-height-1280.jpg, whose height is 1280px .|A validation message will say "Images with height over 1000px can't be uploaded."|A validation message will say "Images with height over 1000px can't be uploaded."|pass|[image](./images/manual-tests/DRF-profiles/6.png)|2023/8/5|
|7|file width validation||Upload ‘image-width-1300.jpg, whose width is 1300px .|A validation message will say "Images with width over 1000px can't be uploaded."| A validation message will say "Images with width over 1000px can't be uploaded."|pass|[image](./images/manual-tests/DRF-profiles/7.png)|2023/8/5|
|8|Profile can't be updated by other users |Log out and log in as user1| Go to "/profiles/1" |The edit form is absent. |The edit form is absent. | pass|[image1 ](./images/manual-tests/DRF-profiles/4-1.png)[image](./images/manual-tests/DRF-profiles/5.png)|2023/7/29|

### Poems

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can't create poems if not logged in. | Log out. | Check if the form is displayed. | The form is absent. |The form is absent.| pass|[image](./images/manual-tests/DRF-poems/1.png)|2023/7/29|
|2|Can create poems if logged in. | Log in as user1. | Enter title: title; content: content; category: other; publish: false; and click 'post.' | The new poem 'title' is created.|The new poem 'title' is created.| pass|[image](./images/manual-tests/DRF-poems/2.png)|2023/7/29|
|3|Can update poems |Go to "/poems/7"| Enter title: title updated; content: content updated; category: nature; publish: true; and click 'PUT.' | The poem data is updated.|The poem data is updated.| pass|[image](./images/manual-tests/DRF-poems/3.png)|2023/7/29|
|4|Other users cannot update poems. |Log in as admin and go to "/poems/7"| Check if the edit form is absent | The edit form is absent.|The edit form is absent.| pass|[image](./images/manual-tests/DRF-poems/4.png)|2023/7/29|
|5|Owners can delete their own poems. |Log in as user1 and go to "/poems/7"| Click 'Delete' and go to "/poems/7" | The poem will not be found.|A note indicates 404 error, and that the poem is 'not found.'| pass|[image](./images/manual-tests/DRF-poems/5.png)|2023/7/29|

### Comments
- log in as user1 and make a poem (title: poem 1; content: content; category: 'other'; publish: true)

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can create comments | Log in as admin | Select 'poem 1' and enter 'hello' for content.  Click 'Post.'|Comment 'hello' is created. |Comment 'hello' is created. | pass|[image](./images/manual-tests/DRF-comments/1.png)|2023/7/29|
|2|Can edit comments |--| Update as follows: content: 'hello updated'; Click 'Put.'|Comment is updated. |Comment is updated. | pass|[image](./images/manual-tests/DRF-comments/2.png)|2023/7/29|
|3|can't update comments if logged out |Log out. Go to "/comments/9"| Check if the edit form is present.|The edit form is absent. |The edit form is absent. | pass|[image](./images/manual-tests/DRF-comments/3.png)|2023/7/29|
|4|Other members can't update comments. |Log in as admin. Go to "/comments/| Check if the edit form is present.|The edit form is absent. |The edit form is absent. | pass|[image](./images/manual-tests/DRF-comments/4.png)|2023/7/29|
|5|Can delete one's own comments |log in as admin and go to "/comments/10 |Click 'Delete'|Comment is deleted. |Comment is deleted. | pass|[image](./images/manual-tests/DRF-comments/5.png)|2023/7/29|

### Likes

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can't like poems if not logged in. | Log out. Go to "/poems." |Check if the form is displayed.|The form is absent. |The form is absent. | pass|[image](./images/manual-tests/DRF-likes/1.png)|2023/7/29|
|2|Can like poems if logged in. | Log in as admin. Go to "/likes" |Select 'poem 1' and click 'POST' |Like object is made.|Like object with values owner: admin; poem: 8 (id of 'poem 1') is made. | pass|[image](./images/manual-tests/DRF-likes/2.png)|2023/7/29|
|3|Can't like the same poem twice |--|Select 'poem 1' and click 'POST' |Error will be raised.|Error "possible duplicated" is raised (400 Bad request) |pass|[image](./images/manual-tests/DRF-likes/3.png)|2023/7/29|
|4|Can like one's own poems | Log in as user1. Go to "/likes" |Select 'poem 1' and click 'POST' |Like object is created.|Like object with values owner: user1; poem: 8 (id of 'poem 1') is created. | pass|[image](./images/manual-tests/DRF-likes/2.png)|2023/7/29|
|5|Can delete own like objects | Log in as user1. Go to "/likes/4" (owner: user1; poem: 8)|Click 'Delete' |Like object is deleted.|Like object is deleted. | pass|[image](./images/manual-tests/DRF-likes/5.png)|2023/7/29|

### Followers

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can't follow users if not logged in. | Log out. Go to "/followers" |Check if the form is displayed. |The form is absent. |The form is absent. | pass|[image](./images/manual-tests/DRF-followers/1.png)|2023/7/29|
|2|Can follow users if logged in. | Log in as admin. Go to "/followers" |Select 'user1' and click 'POST' |Follow object is made.|Follow object with values owner: admin; followed_name: user1 is made. | pass|[image](./images/manual-tests/DRF-followers/2.png)|2023/7/29|
|3|Can't follow the same user twice |--|Select 'user1' and click 'POST' |Error will be raised.|Error "possible duplicated" is raised (400 Bad request) |pass|[image](./images/manual-tests/DRF-followers/4.png)|2023/7/29|
|4|Can follow onself |--|Select 'admin' and click 'POST' |A new Follower object is made.|Follower object with values owner: admin and followed_name: admin is created. |pass|[image](./images/manual-tests/DRF-followers/4.png)|2023/7/29|
|5|Can delete one's own Follower object |--|Go to "/followers/4" (owner: admin; followed_name: admin) and click "Delete." |The Follower object is deleted.|The Follower object is deleted. |pass|[image](./images/manual-tests/DRF-followers/5.png)|2023/7/29|

### Check updated fields in profiles

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|followers_counts. | Log out. Go to "/profiles" |Check if followers count for user1 and admin are 1. |The followers counts for user1 and admin are 1. |The followers counts for user1 and admin are 1.| pass|[image](./images/manual-tests/DRF-profiles2/1.png)|2023/7/29|
|2|following_id | Log in as admin and go to "/profiles"|Check the following ids for user1 and for admin. |The following id for user1 is present and following id for admin is null. |The following id for user1 is 3. The following id for admin is null.| pass|[image](./images/manual-tests/DRF-profiles2/2.png)|2023/7/29|
|3| followers_id is null if logged out. | Log out. Go to "/profiles" |Check the following ids for user1 and for admin. |Both following ids are null. |Both following ids are null.| pass|[image](./images/manual-tests/DRF-profiles2/3.png)|2023/7/29|

### Check updated fields in poems
- Log in as admin, go to "/comments" and make a comment with content "hello 2" for poem 1.

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|like_counts | Log out. Go to "/poems/8" |Check the likes count | The likes count is 1. |The likes count is 1.| pass|[image](./images/manual-tests/DRF-poems2/1-3.png)|2023/7/29|
|2|comments_counts | -- |Check the comments count | The comments count is 1. |The comments count is 1.| pass|[image](./images/manual-tests/DRF-poems2/1-3.png)|2023/7/29|
|3|like_id is null if logged out|--|Check the like id of 'poem 8'. |The like id is null. |The like id is null.| pass|[image](./images/manual-tests/DRF-poems2/1-3.png)|2023/7/29|
|4| like id is present if the user has liked the poem. | Log in as admin. Go to "/poems/8" |Check the like id | like_id has a value. |like id is 2.| pass|[image](./images/manual-tests/DRF-poems2/4.png)|2023/7/29|
|5| like id is null if the user hasn't liked or has unliked the poem. | Log in as user1. Go to "/poems/8" |Check the like id | like_id is null. |like id is null.| pass|[image](./images/manual-tests/DRF-poems2/5.png)|2023/7/29|

## Testing Code
I checked all modules in the CI python linter at https://pep8ci.herokuapp.com
All errors were cleared.

## Deployment Process

1.	Create a database (I used ElephantSQL.)
2.	Log in at Heroku, click ‘New’ > ‘Create new app’
3.	Name the app, select the region and click ‘Create app.’
4.	Open the Settings tab.  Add a Config Var DATABASE_URL and enter the database URL without quotation marks.
5.	At the terminal, install dj_database_url==0.5.0 psycopg2
6.	In settings.py underneath the line ‘import os,’ add import dj_database_url<br>
`import os`<br>
`import dj_database_url`

7.	update the DATABASES section to the following:<br>
<img src="./images/readme/deployment-1.png" alt="code snippets" width="600"/>

8. In env.py write:
`os.environ[‘DATABASE_URL’] = “write in database url”`

9.	In order to check if the database is connected, temporarily comment out os.environ[‘DEV’] = 1 in env.py and add print(‘connected’) at the end of the else statement above.  In the terminal run makemigrations - -dry-run and check if ‘connected’ will be printed in the console.
10.	If connected, run migrate command and create a superuser
11.	On the ElephantSQL page for the database, select ‘BROWSER’ in the navigation on the left column.  Click the Table queries button, select ‘auth_user’ and click ‘Execute.’  Check if the superuser has been created. (This confirms the tables are created in the database.)
12.	In the terminal install gunicorn django-cors-headers and update requirements.txt
13.	Make Procfile and write these two lines:<br>
`release: python manage.py makemigrations && python manage.py migrate`<br>
`web: gunicorn drf_api.wsgi`
14.	In settings.py update the allowed hosts values to include the url of the Heroku app:<br>
`ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']`
15.	In the installed apps section, add ‘corsheaders’ below ‘dj_rest_auth.registration’<br>
16.	Add corsheaders middleware to the TOP of the MIDDLEWARE
`'corsheaders.middleware.CorsMiddleware',`
17.	Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:<br>
<img src="./images/readme/2.png" alt="code snippets" width="600"/>
18.	In order to enable sending cookies in cross-origin requests so that users can get authentication functionality, add the follwoing:<br>
`CORS_ALLOW_CREDENTIALS = True`
19.	To be able to have the front end app and the API deployed to different platforms, set the JWT_AUTH_SAMESITE attribute to 'None'. (Without this the cookies would be blocked.)<br>
<img src="./images/readme/3.png" alt="code snippets" width="600"/>
20. Remove the value for SECRET_KEY and replace with the following code to use an environment variable instead.<br>
`SECRET_KEY = os.environ.get('SECRET_KEY')`
21.	Set a NEW value for the SECRET_KEY environment variable in env.py.<br>
`os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")`
22.	In settings.py add the URL of the Heroku app to allowed hosts.<br>
`ALLOWED_HOSTS = [ os.environ.get('ALLOWED_HOST'),]`
23.	Comment again the environment variable ‘DEV’ in env.py
24.	Run pip freeze –local > requirements.txt command to confirm the requirements.txt is up to date.
25.	Add, commit and push to Github.
26.	On Heroku dashboard on the Settings tab, make following Config Var:
- SECRET_KEY and CLOURDINARY_URL (with no quotation marks)
- DISABLE_COLLECTSTATIC = 1
- ALLOWED_HOST (enter the URL of the Heroku app)
27.	Open the Deploy tab, select connect to Github.  Search for the repository and click ‘Connect.’
28.	Click ‘Deploy’ at the bottom of the page.
29.	If message ‘Your app was successfully deployed’ appears, click “View.”

### Credits:

I leaned Django Rest Framework from the walk-through project at CI, and I incorporated many ideas from it.<br>
https://github.com/Code-Institute-Solutions/drf-api
