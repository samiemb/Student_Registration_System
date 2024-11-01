from django.db import models
from course_catalog.models import Courses  # Make sure this is correct

class CourseReport(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)  # Reference to Courses
    student_count = models.PositiveIntegerField()
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.course} - {self.student_count} students"



