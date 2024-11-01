# reporting_analytics/views.py
from django.shortcuts import render
from payment_processing.models import Payment
from course_catalog.models import Courses
from django.db.models import Sum
from datetime import datetime

def payment_summary(request):
    total_payments = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    payments = Payment.objects.all()
    context = {
        'total_payments': total_payments,
        'payments': payments,
    }
    return render(request, 'reporting_analytics/payment_summary.html', context)

def course_enrollment_report(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'reporting_analytics/course_enrollment_report.html', context)
def report_view(request):
    payments = Payment.objects.all()  # Fetch all payments; you can filter if needed
    context = {
        'payments': payments,
        'current_year': datetime.now().year,
    }
    return render(request, 'reporting_analytics/report.html', context)


