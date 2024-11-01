from django.contrib import admin
from django.urls import path, include
from .views import redirect_to_user  # Import the redirect view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_gateway.urls')),
    path('user/', include('user_management.urls')),
    path('courses/', include('course_catalog.urls')),
    path('payment/', include('payment_processing.urls')),
    path('reports/', include('reporting_analytics.urls')),
    path('', redirect_to_user, name='root_redirect'),
]