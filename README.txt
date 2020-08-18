Feature covered:
(1) User authentication
(2) Session sensitive coutndown timer
(3) Show score upon submit
(4) Exam Duration, User can be changed or added from django admin panel

Pre-requsite: Python 3.7 or above

To Run The project:

(1) Create a virtual environment for the project (https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)
(2) Install required libraries from requirements.txt (you can use pip install -r requirements.txt )
(3) Create a DataBase in mysql and name it "online_exam" (without quotes)
(4) Open settings.py of PROJECT_ONLINE_EXAM directory
(5) Change USER, PASSWORD of DATABASES parameter as per your environment
(6) Activate venv and navigate to PROJECT_ONLINE_EXAM directory
(7) Run django migrations:
		python manage.py makemigrations app_user
		python manage.py makemigrations app_quiz
		python manage.py migrate
(8) Import some dummy data from user_question_duration.sql. You Can PhpmyAdmin or whatever you comfortable with
(9) Run projet: python manage.py runserver
(10) Go to localhost:8000
(11) login with a dummy user (username: mizan, pass:1234)

Additional Note: 

You can chekout django admin panel from localhost:8000/admin incase want to change/add exam duaration, user or modify table coantent easily.

For that first you need to create a superuser using folowing command:

python manage.py createsuperuser

Then follow the subsequent steps on the pormt


In case of any issue, feedback or suggestion you can mail back to : ridwanmizan@gmail.com
	