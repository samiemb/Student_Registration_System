# student_registration_system/views.py

from django.shortcuts import redirect

def redirect_to_user(request):
    return redirect('/user/')
