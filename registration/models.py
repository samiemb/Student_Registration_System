from django.db import models
from user_management.models import CustomUser
from course_catalog.models import Courses

class Registration(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} - {self.course}'
