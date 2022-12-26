from django.urls import path
from . import views


urlpatterns =[
    path('', views.default_endpoint, name='home'), 
    path('developers/', views.developers, name='developers'),
    path('developers/<str:username>/', views.developer_detail, name='developer_details')
]