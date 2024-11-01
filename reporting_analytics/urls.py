from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_view, name='report_view'),
    path('payment-summary/', views.payment_summary, name='payment_summary'),
    path('course-enrollment-report/', views.course_enrollment_report, name='course_enrollment_report'),
]
