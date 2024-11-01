from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    enrollment_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username
