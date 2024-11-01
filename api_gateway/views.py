import requests
from django.http import JsonResponse

def payment_view(request):
    try:
        # Forward the request to the payment processing service
        response = requests.get('http://127.0.0.1:8001/payment/')
        response.raise_for_status()  # Raise an error for bad responses
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def registration_view(request):
    response = requests.get('http://localhost:8002/registration/')  # Microservice URL
    return JsonResponse(response.json())

def course_catalog_view(request):
    response = requests.get('http://localhost:8003/courses/')  # Microservice URL
    return JsonResponse(response.json())
def user_management_view(request):
    try:
        # Forward the request to the user management service
        response = requests.get('http://localhost:8002/user/')  # Ensure the correct URL
        response.raise_for_status()  # Raise an error for bad responses
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def reporting_analytics_view(request):
    try:
        # Forward the request to the reporting analytics service
        response = requests.get('http://localhost:8003/reports/')  # Ensure the correct URL
        response.raise_for_status()  # Raise an error for bad responses
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
