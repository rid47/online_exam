from django.shortcuts import redirect


def login_required(function):
    def wrapper(request, *args, **kw):
        if not ('logged_in' in request.session and request.session['logged_in'] is True):
            return redirect('app_user:logout')
        else:
            return function(request, *args, **kw)
    return wrapper
