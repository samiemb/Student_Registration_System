from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Amount')
    card_number = forms.CharField(max_length=16, label='Card Number')
    expiry_date = forms.DateField(label='Expiry Date (YYYY-MM-DD)')
    cvv = forms.CharField(max_length=3, label='CVV')
