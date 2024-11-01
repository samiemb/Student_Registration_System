from django.shortcuts import render
from .models import Courses

def course_list(request):
    courses = Courses.objects.all()  # Fetch all courses
    return render(request, 'course_catalog/course_list.html', {'courses': courses})

