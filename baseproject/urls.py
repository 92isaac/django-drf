from django.urls import path
from . import views


urlpatterns =[
    path('', views.default_endpoint, name='home'), 
    path('users/', views.users, name='users'),
    path('users/<str:username>/', views.user_detail, name='users_details')
]