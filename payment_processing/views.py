# payment_processing/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Here you would handle the payment processing logic
            # For example, you could save the payment information to the database
            # and redirect to a success page
            return redirect('payment_success', payment_id=1)  # Replace with actual payment ID
    else:
        form = PaymentForm()
    return render(request, 'payment_processing/payment.html', {'form': form})

def payment_success(request, payment_id):  # Make sure to include payment_id here
    return render(request, 'payment_processing/payment_success.html', {'payment_id': payment_id})
def process_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        # Simulate payment processing
        # Here, you would integrate with a real payment gateway like Stripe or PayPal
        payment.status = 'completed'
        payment.save()

        return redirect('payment:payment_success', payment_id=payment.id)

    return render(request, 'payment_processing/process_payment.html', {'payment': payment})
def payment_history(request):
    payments = Payment.objects.all()  # Retrieve all payments
    return render(request, 'payment_history.html', {'payments': payments})