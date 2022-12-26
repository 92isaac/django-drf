from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Developer
from .serializers import DeveloperSerializer

# Create your views here.
# def default_endpoint(request):
#     data = ['developers', '/developer/:details']
#     return JsonResponse(data, safe=False)
    

# def developers(request):
#     data = ['tayo', 'isaac', 'tumininu', 'lawyer kunle', 'rowland']
#     return JsonResponse(data, safe=False)

# def developer_detail(request, username):
#     data = username
#     return JsonResponse(data, safe=False)

@api_view(['GET'])
def default_endpoint(request):
    data = ['developers', '/developer/:details']
    return Response(data)
    
@api_view(['GET'])
def developers(request):
    # data = ['tayo', 'isaac', 'tumininu', 'lawyer kunle', 'rowland']
    # using object,all or object.filter to get all and query as well
    # developers = Developer.objects.all()

    developers = Developer.objects.filter()
    serializer = DeveloperSerializer(developers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def developer_detail(request, username):
    # data = username
    developer = Developer.objects.get(username=username)
    serializer = DeveloperSerializer(developer)
    return Response(serializer.data)