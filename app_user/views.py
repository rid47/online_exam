from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from datetime import datetime, timedelta
from app_quiz.models import Question, Duration
# Create your views here.


def login(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            # print("logged_in")
            return redirect("app_quiz:question")
    else:
        return render(request, 'user/login.html')


def login_validate(request):
    if request.method == 'POST':
        password = request.POST['pass']
        username = request.POST['username']
        # print(f"username: {username} & Password: {password}")
        try:
            user = User.objects.get(name=username, password=password)

        except User.DoesNotExist:
            user = None

        if user is None:
            messages.error(request, 'Username/Password Incorrect !')
            return render(request, 'user/login.html', dict(username=username, password=password))
        else:
            request.session['logged_in'] = True
            request.session['user_name'] = user.name
            request.session['end_time'] = get_end_time()
            request.session['ans_submitted'] = False
            request.session['score'] = 0
            request.session['no_of_q'] = Question.objects.count()
            return redirect("app_quiz:question")


def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
    if 'user_name' in request.session:
        del request.session['user_name']
    if 'end_time' in request.session:
        del request.session['end_time']
    if 'ans_submitted' in request.session:
        del request.session['ans_submitted']
    if 'score' in request.session:
        del request.session['score']
    if 'no_of_q' in request.session:
        del request.session['no_of_q']
    return redirect('app_user:login')


def get_end_time():
    """ Return Exam End time starting from
        Login time """
    try:
        set_end_time = Duration.objects.latest('id').time_in_minutes
    except Duration.DoesNotExist:
        set_end_time = 1

    login_time = datetime.now()
    end_time_obj = login_time + timedelta(minutes=set_end_time)
    end_time_str = end_time_obj.strftime("%b %d, %Y %H:%M:%S")  # format to match front end js format
    return end_time_str
