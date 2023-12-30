from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('',EmployeeListview.as_view(),name='list'),
    path('create',EmployeeCreateview.as_view(),name='create'),
    path('update/<int:pk>',EmployeeUpdateview.as_view(),name='update'),
    path('delete/<int:pk>',EmployeeDeleteview.as_view(),name='delete')
]