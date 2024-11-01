# registration/views.py

from django.shortcuts import redirect
from .models import Registration  # Your registration model
from payment_processing.models import Payment  # Your payment model


def register_course(request, course_id):
    # Handle course registration logic
    if request.method == 'POST':
        # Assuming the user has been authenticated and is logged in
        user = request.user
        course = Course.objects.get(id=course_id)

        # Register the course for the user (you might already have a registration system)
        registration = Registration(user=user, course=course)
        registration.save()

        # Redirect the user to the payment page after successful registration
        # Here, you create a payment record and send the user to the payment page
        payment = Payment.objects.create(user=user, course=course, amount=course.fee, status='pending')
        return redirect('payment:process_payment',
                        payment_id=payment.id)  # Assuming 'process_payment' is your payment view

    return render(request, 'registration/register_course.html', {'course': course})

