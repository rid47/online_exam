Feature covered:
(1) User authentication
(2) Session sensitive countdown timer
(3) Show score upon submit
(4) Exam Duration, User, Question can be changed or added from django admin panel

Pre-requisite: Python 3.7 or above

To Run The project:

(1) Download zip file then unzip or clone the project.
(1) Create a virtual environment for the project
    (https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
(2) Install required libraries from requirements.txt
    (you can use pip install -r requirements.txt command )
(3) Create a DataBase in mysql and name it "online_exam" (without quotes)
(4) Open settings.py of PROJECT_ONLINE_EXAM directory
(5) Change USER, PASSWORD of DATABASES parameter as per your environment
(6) Activate virtual environment and navigate to project directory where manage.py file is situated
(7) Run django migrations:
		python manage.py makemigrations app_user
		python manage.py makemigrations app_quiz
		python manage.py migrate
(8) Import some dummy data to online_exam database from user_question_duration.sql file,
    You Can user phpMyAdmin or whatever you are comfortable with
(9) Run project using the command: python manage.py runserver
(10) Go to localhost:8000 on your web browser
(11) login with a dummy user (username: mizan, password :1234)

Additional Note: 

You can checkout django admin panel from localhost:8000/admin in case
you want to change/add exam duration, user or may be questions easily.

For that first you need to create a superuser using following command:

python manage.py createsuperuser

Then follow the subsequent steps on the command prompt


In case of any issues, feedback or suggestions you can always mail back to : ridwanmizan@gmail.com
	