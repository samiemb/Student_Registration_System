from django.urls import path
from .views import payment_view, registration_view, course_catalog_view, user_management_view, reporting_analytics_view

urlpatterns = [
    path('payment/', payment_view, name='payment'),
    path('registration/', registration_view, name='registration'),
    path('courses/', course_catalog_view, name='courses'),
    path('user/', user_management_view, name='user_management_view'),
    path('reports/', reporting_analytics_view, name='reporting_analytics_view'),
]
