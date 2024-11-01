from django.urls import path
from . import views
from .views import payment_view, payment_success, payment_history
urlpatterns = [
    path('', payment_view, name='payment'),
    path('process/<int:payment_id>/', views.process_payment, name='process_payment'),
    path('success/<int:payment_id>/', views.payment_success, name='payment_success'),
    path('history/', payment_history, name='payment_history'),
]
