from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def default_endpoint(request):
    data = ['users', '/user/:details']
    return JsonResponse(data, safe=False)
    

def users(request):
    data = ['tayo', 'isaac', 'tumininu', 'lawyer kunle', 'rowland']
    return JsonResponse(data, safe=False)

def user_detail(request, username):
    data = username
    return JsonResponse(data, safe=False)