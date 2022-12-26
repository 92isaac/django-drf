from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Developer
from .serializers import DeveloperSerializer
from django.db.models import Q

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
    
@api_view(['GET', 'POST', 'PUT'])
def developers(request):
    # data = ['tayo', 'isaac', 'tumininu', 'lawyer kunle', 'rowland']
    # developers = Developer.objects.all()

    # using object.all over object.filter to get all and query as well e.g http://127.0.0.1:5050/developers/?query=react

    # conditional statements to check what leb\vel of restdullness the api is 
    # if request is get request
    if request.method == 'GET':
        query = request.GET.get('query')
        if query is None:
            query = ''

        developers = Developer.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        create_developer = Developer.objects.create(username=request.data['username'], bio=request.data['bio'])
        serializer =DeveloperSerializer(create_developer, many=False)
        return Response(serializer.data)
        # return Response('developer added successfully')


    
# @api_view(['POST'])
# def add_developer(request):
#     Developer.objects.create(username=request.data['username'])
#     return Response('developer added successfully')

@api_view(['GET', 'PUT', 'DELETE'])
def developer_detail(request, username):
    # data = username
    developer = Developer.objects.get(username=username)
    if request.method == 'GET':
        # developer = Developer.objects.get(username=username)
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)
    if request.method == 'PUT':
        developer.username = request.data['username']
        developer.bio = request.data['bio']
        developer.save()
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)

    if request.method == 'DELETE':
        developer.delete()
        return Response("Developer deleted")

# its not a must every api is restful
# rest api, fast api,  soap api type of apis are just structures of building api