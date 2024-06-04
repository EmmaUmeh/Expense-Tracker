from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from.models import *
import json
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@csrf_exempt
def my_view(request):
    # Access the CSRF token from the request object
    csrf_token = request.META.get("CSRF_COOKIE", "")
    
    # Print the CSRF token to the console
    print("CSRF Token:", csrf_token)

    # Return the CSRF token in a JSON response
    return JsonResponse({"csrf_token": csrf_token})

@csrf_exempt
def home(request):
    return JsonResponse({"message": "Welcome to Smart Expense Tracker!"}, safe=False)

@csrf_exempt
def Register_User(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Decode bytes to string before parsing JSON

            username = data.get('username')
            email = data.get('email')
            phone_Number = data.get('phone_Number')
            password = data.get('password')

            if not (username and email and phone_Number and password):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'User with this email already exists'}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'User with this username already exists'}, status=400)

            user = User.objects.create(username=username, email=email, phone_Number=phone_Number, password=password)
            user.save()

            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                'data': [data],
                'message': 'User registered successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
                
            }, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def Login_User(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))  # Decode bytes to string before parsing JSON
            email = data.get('email')
            password = data.get('password')

            user = authenticate(request, username=email, password=password)  # Pass the request object

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, safe=False)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def CreateBudget(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            budget_create = []

            budget_name = data.get('budget_name')
            budget_price = data.get('budget_price')
            budget_date = data.get('budget_date')

            budget_create.append({
                'budget_name': budget_name,
                'budget_price': budget_price,
                'budget_date': budget_date,
            })

            # Corrected the condition to check if the list is empty
            if len(budget_create) > 0:
                return JsonResponse({
                    'data': data,
                    'message': 'Budget Created Successfully'
                })
            else:
                return JsonResponse({'error': 'Error while Creating Budget'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
